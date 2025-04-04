from enum import Enum

class JobType(Enum):
    FULL_TIME = (
        "fulltime", "períodointegral", "estágio/trainee", "tiempocompleto", "vollzeit",
        "voltijds", "tempointegral", "全职", "plnýúvazek", "fuldtid", "دوامكامل",
        "kokopäivätyö", "tempsplein", "πλήρηςαπασχόληση", "teljesmunkaidő", "tempopieno",
        "heltid", "jornadacompleta", "pełnyetat", "정규직", "100%", "全職", "งานประจำ",
        "tamzamanlı", "повназайнятість", "toànthờigian",
    )
    PART_TIME = ("parttime", "teilzeit", "částečnýúvazek", "deltid")
    CONTRACT = ("contract", "contractor")
    TEMPORARY = ("temporary",)
    INTERNSHIP = ("internship", "prácticas", "ojt(onthejobtraining)", "praktikum", "praktik")
    PER_DIEM = ("perdiem",)
    NIGHTS = ("nights",)
    OTHER = ("other",)
    SUMMER = ("summer",)
    VOLUNTEER = ("volunteer",)