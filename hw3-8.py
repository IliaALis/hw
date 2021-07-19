
import random



class Pinguin:
    

    def __init__(self, **kwargs) -> None:
        self.__kind_of_pinguin = kwargs.get('kind', None)
        self.__kind_of_body = kwargs.get('body_', None)
        self.__where_is = kwargs.get('where', None)
     
    def __str__(self) -> str:
        # return "kinde:{} pinguin timidly hides body_:{} where: {}".format(self.__kind_of_pinguin, self.__kind_of_body, self.__where_is)
        return "{} pinguin timidly hides body {} {}".format(self.__kind_of_pinguin, self.__kind_of_body, self.__where_is)

  
    @property
    def kind_of_pinguin(self):
        return self.__kind_of_pinguin

    @kind_of_pinguin.setter
    def kind_of_pinguin(self):
        value = random.randint(1,3)
        if value == 1:
            self.__kind_of_pinguin = 'stupid'
            return self.__kind_of_pinguin
        elif value == 2:
            self.__kind_of_pinguin = 'clever'
            return self.__kind_of_pinguin
        else:
            self.__kind_of_pinguin = 'bald head'
            return self.__kind_of_pinguin

    @property
    def kind_of_body(self):
        return self.__kind_of_body

    @kind_of_body.setter
    def kind_of_body(self):
        value = random.randint(1,3)
        if value == 1:
            self.__kind_of_body = 'fat'
            return self.__kind_of_body
        elif value == 2:
           self.__kind_of_body = 'red'
           return self.__kind_of_body
        else:
            self.__kind_of_body = 'bad'
            return self.__kind_of_body

    @property
    def where_is(self):
        return self.__where_is

    @where_is.setter
    def where_is(self):
        value = random.randint(1,3)
        if value == 1:
            self.__where_is = 'in the cliffs'
            return self.__where_is
        elif value == 2:
           self.__where_is = 'in torros'
           return self.__where_is
        else:
            self.__where_is = 'in a refrigerator'
            return self.__where_is

if __name__ == "__main__":
    
    albatross = Pinguin(kind_of_pinguin='kind', kind_of_body="body_",  whre_is='where')
     

    albatross.kind_of_body
    
    albatross.kind_of_pinguin
    
    albatross.where_is
    print(albatross)
  