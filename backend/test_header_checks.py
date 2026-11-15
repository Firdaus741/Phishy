"""Plain tests for header_checks.py. Run: python backend\\test_header_checks.py"""
from header_checks import check_headers, registered_domain

GMAIL_PASS = (
    "mx.google.com; dkim=pass header.i=@paypal.com header.s=pp-dkim1 header.b=abc123; "
    "spf=pass (google.com: domain of service@paypal.com designates 1.2.3.4 as permitted sender) "
    "smtp.mailfrom=service@paypal.com; dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=paypal.com"
)
GMAIL_FAIL = (
    "mx.google.com; dkim=fail header.i=@evil.com; "
    "spf=softfail (google.com: domain of transitioning x@evil.com does not designate 5.6.7.8 as permitted sender) "
    "smtp.mailfrom=x@evil.com; dmarc=fail (p=NONE sp=NONE dis=NONE) header.from=evil.com"
)
FORGED = "evil-server.example.net; spf=pass smtp.mailfrom=x@paypal.com; dkim=pass; dmarc=pass"


def mail(**kw):
    base = {"from": "", "reply_to": "", "authentication_results": ""}
    base.update(kw)
    return base


def test_registered_domain():
    assert registered_domain("mail.paypal.com") == "paypal.com"
    assert registered_domain("secure.maybank2u.com.my") == "maybank2u.com.my"
    assert registered_domain("example.com") == "example.com"


def test_gmail_pass_is_clean():
    r = check_headers(mail(**{"from": '"PayPal" <service@paypal.com>', "authentication_results": GMAIL_PASS}))
    assert r["auth_verified"] and (r["spf"], r["dkim"], r["dmarc"]) == ("pass", "pass", "pass")
    assert not r["suspicious"] and r["reasons"] == []


def test_gmail_failures_are_flagged():
    r = check_headers(mail(**{"from": "x@evil.com", "authentication_results": GMAIL_FAIL}))
    assert r["auth_failed"] and r["suspicious"]
    assert (r["spf"], r["dkim"], r["dmarc"]) == ("softfail", "fail", "fail")


def test_forged_authentication_results_are_ignored():
    r = check_headers(mail(**{"from": "x@paypal.com", "authentication_results": FORGED}))
    assert not r["auth_verified"]
    assert not r["auth_failed"]
    assert any("not from Gmail" in x for x in r["reasons"])


def test_forged_fail_from_other_server_does_not_flag():
    r = check_headers(mail(**{"from": "a@b.com", "authentication_results": "evil.net; spf=fail; dmarc=fail"}))
    assert not r["auth_failed"] and not r["suspicious"]


def test_missing_authentication_results():
    r = check_headers(mail(**{"from": "a@b.com"}))
    assert not r["auth_verified"] and (r["spf"], r["dkim"], r["dmarc"]) == ("none", "none", "none")
    assert not r["suspicious"] and r["reasons"] == []


def test_dkim_any_pass_wins():
    auth = "mx.google.com; dkim=fail header.i=@a.com; dkim=pass header.i=@b.com; spf=pass; dmarc=pass"
    assert check_headers(mail(**{"from": "x@b.com", "authentication_results": auth}))["dkim"] == "pass"


def test_brand_impersonation():
    r = check_headers(mail(**{"from": '"PayPal Support" <help@paypa1-secure.com>'}))
    assert r["display_name_brand_mismatch"] == "paypal" and r["suspicious"]


def test_real_brand_domain_not_flagged():
    assert not check_headers(mail(**{"from": '"Maybank" <alert@maybank2u.com.my>'}))["suspicious"]
    assert not check_headers(mail(**{"from": '"Google" <no-reply@accounts.google.com>'}))["suspicious"]


def test_brand_word_must_be_whole_word():
    assert not check_headers(mail(**{"from": '"Pineapple Club" <hi@example.com>'}))["suspicious"]


def test_reply_to_mismatch_is_weak():
    r = check_headers(mail(**{"from": "service@bank.com", "reply_to": "claims@gmail.com"}))
    assert r["reply_to_mismatch"] and not r["suspicious"]


def test_reply_to_same_organisation_ok():
    r = check_headers(mail(**{"from": "a@mail.bank.com", "reply_to": "support@bank.com"}))
    assert not r["reply_to_mismatch"]


if __name__ == "__main__":
    tests = [f for name, f in sorted(globals().items()) if name.startswith("test_")]
    for t in tests:
        t()
        print("ok  ", t.__name__)
    print(f"\n{len(tests)} tests passed")
