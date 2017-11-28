class Market(dict):
    a = 1

    def list_all_member(self):
        bb = {
            "c" : "Hello"
        }
        for name, value in vars(self.__class__).items():
            print('%s=%s' % (name, value))
        print(dict(vars(self.__class__).items()))

if __name__ == '__main__':
    market = Market()
    print(market.a)
    market.list_all_member()
