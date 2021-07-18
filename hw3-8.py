
import random



class Pinguin:
    # value = random.randint(1,3)
    # print(value)

    def __init__(self, **kwargs) -> None:
        self.__kinde_of_pinguin = kwargs.get('kinde', None)
        self.__kinde_of_body = kwargs.get('body_', None)
        self.__where_is = kwargs.get('where', None)
     
    def __str__(self) -> str:
        # return "kinde:{} pinguin timidly hides body_:{} where: {}".format(self.__kinde_of_pinguin, self.__kinde_of_body, self.__where_is)
        return "{} pinguin timidly hides body {} {}".format(self.__kinde_of_pinguin, self.__kinde_of_body, self.__where_is)

  
    @property
    def kinde_of_pinguin(self):
        return self.__kinde_of_pinguin

    @kinde_of_pinguin.setter
    def kinde_of_pinguin(self):
        v = random.randint(1,3)
        if v == 1:
            self.__kinde_of_pinguin = 'stupid'
            return self.__kinde_of_pinguin
        elif v == 2:
            self.__kinde_of_body = 'clever'
            return self.__kinde_of_pinguin
        else:
            self.__kinde_of_body = 'bald head'
            return self.__kinde_of_pinguin

    @property
    def kinde_of_body(self):
        return self.__kinde_of_body

    @kinde_of_body.setter
    def kinde_of_body(self):
        val = random.randint(1,3)
        if val == 1:
            self.__kinde_of_body = 'fat'
            return self.__kinde_of_body
        elif val == 2:
           self.__kinde_of_body = 'red'
           return self.__kinde_of_body
        else:
            self.__kinde_of_body = 'bad'
            return self.__kinde_of_body

    @property
    def where_is(self):
        return self.__where_is

    @where_is.setter
    def where_is(self):
        va = random.randint(1,3)
        if va == 1:
            self.__where_is = 'in the cliffs'
            return self.__where_is
        elif va == 2:
           self.__where_is = 'in torros'
           return self.__where_is
        else:
            self.__where_is = 'in a refrigerator'
            return self.__where_is

if __name__ == "__main__":
    # value = random.randint(1,3)
    albatross = Pinguin(kinde_of_body="body_", kinde_of_pinguin='kinde', whre_is='where')
    
    # print(albatross)

    albatross.kinde_of_body
    # print(albatross)
    albatross.kinde_of_pinguin
    # print(albatross)
    albatross.where_is
    print(albatross)
  