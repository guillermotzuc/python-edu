from datetime import datetime, timedelta
from datetime import date

# DataClass
class DataClass(type):
    def __new__(cls, name, bases, dct):
        final = super().__new__(cls, name, bases, dct)

       # import pdb; pdb.set_trace()

        defaults = {
            key : value
            for key, value in final.__dict__.items()
            if not key.startswith("_")
        }

        init = final.__create_init(final.__annotations__, defaults)
        setattr(final, "__init__", init)

        def eq(self, other):
            return self.__dict__ == other.__dict__
        
        def ne(self, other):
            return self.__dict__ != other.__dict__
        
        setattr(final, "__init__", init)
        setattr(final, "__eq__", eq)
        setattr(final, "__ne__", ne)

        return final
    
    @staticmethod
    def __create_init(annotations, defaults, *, return_type=None):
        name = "__init__"
        args = ["self"]
        default_args = []
        body_lines = []
        for key, value in annotations.items():
            if key in defaults.keys():
                #"release_date:datetime.date=datetime.date.today()"
                default_args.append(f"{key}:{value.__name}=repr(defaults[key])")
            else:
                args.append(f"{key}:{value.__name__}")
            
            body_lines.append(f"self.{key} = {key}")
        
        args = ", ".join(args + default_args)
        body = "\n ".join(body_lines)

        text = f"def {name({args})}->{return_type}\n {body}"
        exec(text)
        return locals()[name]


class Record(metaclass=DataClass):
    artist: str
    title: str
    release_date: datetime.date = date.today()
    album_color: str = "blue"

record1 = Record("The beatles", "with the beatles", datetime.date(1963, 11, 22))
record2 = Record("The beatles", "with the beatles", datetime.date(1963, 11, 22))
record3 = Record("The beatles", "!help")

assert record1.artist == "The beatles"
assert record1.title == "with the beatles"