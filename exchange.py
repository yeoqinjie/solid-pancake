class CurrencyExchange:
    SGDUSD = 0.7
    USDSGD = 1.4

    @classmethod
    def exchange_sgd_usd(cls, amt):
        # if exchange > SGD10, give extra USD1
        if amt > 10:
            result = amt * cls.SGDUSD + 1
        else:
            result = amt * cls.SGDUSD
        return result

    @classmethod
    def exchange_usd_sgd(cls, amt):
        return amt * cls.USDSGD
