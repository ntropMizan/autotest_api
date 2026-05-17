import pytest
#
#
# # @pytest.mark.smoke
# # def test_smoke_case():
# #     assert 1 + 1 == 2
# #
# #
# # @pytest.mark.regression
# # def test_regression_case():
# #     assert 2 * 2 == 4
#
# # @pytest.mark.regression
# # class TestUserAuthentication:
# #     @pytest.mark.smoke
# #     def test_login(self):
# #         ...
# #
# #     @pytest.mark.slow
# #     def test_password_reset(self):
# #         ...
# #
# #     def test_logout(self):
# #         ...
# #
# # @pytest.mark.smoke
# # @pytest.mark.regression
# # @pytest.mark.critical
# # def test_critical_login():
# #     ...
#
# @pytest.mark.api
# class TestUserInterface:
#     @pytest.mark.smoke
#     @pytest.mark.critical
#     def test_login(self):
#         ...
#
#     @pytest.mark.regression
#     def test_forgot_password(self):
#         ...
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         ...

@pytest.mark.smoke
class TestLogin:
    @pytest.mark.smoke
    def test_valid_login(self):
        pass

    @pytest.mark.regression
    def test_invalid_login(self):
        pass

@pytest.mark.regression
class TestRegistration:
    @pytest.mark.regression
    def test_valid_registration(self):
        pass

    @pytest.mark.smoke
    def test_invalid_registration(self):
        pass

@pytest.mark.smoke
@pytest.mark.regression
class TestCheckout:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_checkout(self):
        pass

    def test_invalid_checkout(self):
        pass

def test_search():
    pass
