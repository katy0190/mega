import Enrolment

registrar = Enrolment.Registrar()

kim = Enrolment.Student('김태연', 100)
lee = Enrolment.Student('이재준', 101)
park = Enrolment.Student('박연진', 102)
moon = Enrolment.Student('문동은', 103)

computer = Enrolment.Course('컴퓨터개론', 1, 3)
manage = Enrolment.Course('경영학개론', 2, 2)

registrar.resister_course(kim, computer.name)
kim.show()