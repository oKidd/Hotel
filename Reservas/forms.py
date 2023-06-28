from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Reservas.models import UserExtraInfo, Reserva, TipoHabitacion, Habitacion


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : "User", 'class':"col-6 display-1 fs-4 mb-4 border border-secondary rounded"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder' : "Correo", 'class':"col-12 display-1 fs-4 mb-4 border border-secondary rounded"}), label="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : "Nombre", 'class':"col-12 display-1 fs-4 mb-4 border border-secondary rounded"}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : "Apellido", 'class':"col-12 display-1 fs-4 mb-4 border border-secondary rounded"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Clave", 'class':"col-12 display-1 fs-4 mb-4 border border-secondary rounded"}), min_length=8, label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Confrimar Clave", 'class':"col-12 display-1 fs-4 mb-4 border border-secondary rounded"}), min_length=8, label="")

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder' : "Correo", 'class':"col-8 display-1 fs-4 mx-auto mb-4 border border-secondary rounded"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Clave", 'class':"col-8 display-1 fs-4 mx-auto mb-4 border border-secondary rounded"}))

class UserRegisterExtraForm(forms.ModelForm):
    class Meta:
        model = UserExtraInfo
        fields = ('pais', 'rut', 'nacimiento', 'telefono')
    
    PAISES = [('', "Seleccione Pais"),("Afganistán","Afganistán"),("Albania","Albania"),("Alemania","Alemania"),("Andorra","Andorra"),("Angola","Angola"),("Antigua y Barbuda","Antigua y Barbuda"),("Arabia Saudita","Arabia Saudita"),("Argelia","Argelia"),("Argentina","Argentina"),("Armenia","Armenia"),("Australia","Australia"),("Austria","Austria"),("Azerbaiyán","Azerbaiyán"),("Bahamas","Bahamas"),("Bangladés","Bangladés"),("Barbados","Barbados"),("Baréin","Baréin"),("Bélgica","Bélgica"),("Belice","Belice"),("Benín","Benín"),("Bielorrusia","Bielorrusia"),("Birmania","Birmania"),("Bolivia","Bolivia"),("Bosnia y Herzegovina","Bosnia y Herzegovina"),("Botsuana","Botsuana"),("Brasil","Brasil"),("Brunéi","Brunéi"),("Bulgaria","Bulgaria"),("Burkina Faso","Burkina Faso"),("Burundi","Burundi"),("Bután","Bután"),("Cabo Verde","Cabo Verde"),("Camboya","Camboya"),("Camerún","Camerún"),("Canadá","Canadá"),("Catar","Catar"),("Chad","Chad"),("Chile","Chile"),("China","China"),("Chipre","Chipre"),("Ciudad del Vaticano","Ciudad del Vaticano"),("Colombia","Colombia"),("Comoras","Comoras"),("Corea del Norte","Corea del Norte"),("Corea del Sur","Corea del Sur"),("Costa de Marfil","Costa de Marfil"),("Costa Rica","Costa Rica"),("Croacia","Croacia"),("Cuba","Cuba"),("Dinamarca","Dinamarca"),("Dominica","Dominica"),("Ecuador","Ecuador"),("Egipto","Egipto"),("El Salvador","El Salvador"),("Emiratos Árabes Unidos","Emiratos Árabes Unidos"),("Eritrea","Eritrea"),("Eslovaquia","Eslovaquia"),("Eslovenia","Eslovenia"),("España","España"),("Estados Unidos","Estados Unidos"),("Estonia","Estonia"),("Etiopía","Etiopía"),("Filipinas","Filipinas"),("Finlandia","Finlandia"),("Fiyi","Fiyi"),("Francia","Francia"),("Gabón","Gabón"),("Gambia","Gambia"),("Georgia","Georgia"),("Ghana","Ghana"),("Granada","Granada"),("Grecia","Grecia"),("Guatemala","Guatemala"),("Guyana","Guyana"),("Guinea","Guinea"),("Guinea ecuatorial","Guinea ecuatorial"),("Guinea-Bisáu","Guinea-Bisáu"),("Haití","Haití"),("Honduras","Honduras"),("Hungría","Hungría"),("India","India"),("Indonesia","Indonesia"),("Irak","Irak"),("Irán","Irán"),("Irlanda","Irlanda"),("Islandia","Islandia"),("Islas Marshall","Islas Marshall"),("Islas Salomón","Islas Salomón"),("Israel","Israel"),("Italia","Italia"),("Jamaica","Jamaica"),("Japón","Japón"),("Jordania","Jordania"),("Kazajistán","Kazajistán"),("Kenia","Kenia"),("Kirguistán","Kirguistán"),("Kiribati","Kiribati"),("Kuwait","Kuwait"),("Laos","Laos"),("Lesoto","Lesoto"),("Letonia","Letonia"),("Líbano","Líbano"),("Liberia","Liberia"),("Libia","Libia"),("Liechtenstein","Liechtenstein"),("Lituania","Lituania"),("Luxemburgo","Luxemburgo"),("Macedonia del Norte","Macedonia del Norte"),("Madagascar","Madagascar"),("Malasia","Malasia"),("Malaui","Malaui"),("Maldivas","Maldivas"),("Malí","Malí"),("Malta","Malta"),("Marruecos","Marruecos"),("Mauricio","Mauricio"),("Mauritania","Mauritania"),("México","México"),("Micronesia","Micronesia"),("Moldavia","Moldavia"),("Mónaco","Mónaco"),("Mongolia","Mongolia"),("Montenegro","Montenegro"),("Mozambique","Mozambique"),("Namibia","Namibia"),("Nauru","Nauru"),("Nepal","Nepal"),("Nicaragua","Nicaragua"),("Níger","Níger"),("Nigeria","Nigeria"),("Noruega","Noruega"),("Nueva Zelanda","Nueva Zelanda"),("Omán","Omán"),("Países Bajos","Países Bajos"),("Pakistán","Pakistán"),("Palaos","Palaos"),("Panamá","Panamá"),("Papúa Nueva Guinea","Papúa Nueva Guinea"),("Paraguay","Paraguay"),("Perú","Perú"),("Polonia","Polonia"),("Portugal","Portugal"),("Reino Unido","Reino Unido"),("República Centroafricana","República Centroafricana"),("República Checa","República Checa"),("República del Congo","República del Congo"),("República Democrática del Congo","República Democrática del Congo"),("República Dominicana","República Dominicana"),("Ruanda","Ruanda"),("Rumanía","Rumanía"),("Rusia","Rusia"),("Samoa","Samoa"),("San Cristóbal y Nieves","San Cristóbal y Nieves"),("San Marino","San Marino"),("San Vicente y las Granadinas","San Vicente y las Granadinas"),("Santa Lucía","Santa Lucía"),("Santo Tomé y Príncipe","Santo Tomé y Príncipe"),("Senegal","Senegal"),("Serbia","Serbia"),("Seychelles","Seychelles"),("Sierra Leona","Sierra Leona"),("Singapur","Singapur"),("Siria","Siria"),("Somalia","Somalia"),("Sri Lanka","Sri Lanka"),("Suazilandia","Suazilandia"),("Sudáfrica","Sudáfrica"),("Sudán","Sudán"),("Sudán del Sur","Sudán del Sur"),("Suecia","Suecia"),("Suiza","Suiza"),("Surinam","Surinam"),("Tailandia","Tailandia"),("Tanzania","Tanzania"),("Tayikistán","Tayikistán"),("Timor Oriental","Timor Oriental"),("Togo","Togo"),("Tonga","Tonga"),("Trinidad y Tobago","Trinidad y Tobago"),("Túnez","Túnez"),("Turkmenistán","Turkmenistán"),("Turquía","Turquía"),("Tuvalu","Tuvalu"),("Ucrania","Ucrania"),("Uganda","Uganda"),("Uruguay","Uruguay"),("Uzbekistán","Uzbekistán"),("Vanuatu","Vanuatu"),("Venezuela","Venezuela"),("Vietnam","Vietnam"),("Yemen","Yemen"),("Yibuti","Yibuti"),("Zambia","Zambia"),("Zimbabue","Zimbabue")]

    pais = forms.ChoiceField(widget=forms.Select(attrs={"class": "col-12 display-1 fs-4 mb-4 border border-secondary rounded", "placeholder": "Nacionalidad", "onchange": "hideRut(this.value)"}), choices=PAISES, label="")
    rut = forms.CharField(widget=forms.TextInput(attrs={"class": "col-12 display-1 fs-4 mb-4 border border-secondary rounded", "placeholder": "Rut", "oninput": "checkRut(this)", "style": "display:none;"}), label="", required=None)
    nacimiento = forms.DateField(widget=forms.DateInput(attrs={"class": "col-12 display-1 fs-4 mb-4 border border-secondary rounded", "type": "date", "placholder": "Fecha de Nacimiento"}), label="")
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "col-12 display-1 fs-4 mb-4 border border-secondary rounded", "placeholder": "Telefono"}), label="")

class CrearHabitacion(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ('personas', 'tipo', 'valor', 'caracteristicas')
    
    personas = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "style" : "border: none; outline: none;"}))
    tipo = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "style" : "border: none; outline: none;"}), queryset=TipoHabitacion.objects.all())
    #.values_list('tipo', flat=True)
    valor = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "style" : "border: none; outline: none;"}), label="Valor (CLP)")
    caracteristicas = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"rows": "1", "class": "w-100 text-center fs-4 display-1 mb-1", "style" : "border: none; outline: none;"}))

class ReservaForm(forms.ModelForm):
  class Meta:
    model = Reserva
    fields = ('adultos', 'fecha_inicio', 'ninos', 'fecha_termino')

  ADULTOS = [("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5")]
  NINOS = [("0", "0"),("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5")]

  adultos = forms.ChoiceField(widget=forms.Select(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "style" : "border: none;"}), choices=ADULTOS, label="Cantidad Adultos")
  ninos = forms.ChoiceField(widget=forms.Select(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "style" : "border: none;"}), choices=NINOS, label="Cantidad Ninos")
  fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "type" : "date", "style" : "border: none;", "onchange":"setMinDate(this)"}), label="Fecha Inicio Uso")
  fecha_termino = forms.DateField(widget=forms.DateInput(attrs={"class": "w-100 text-center fs-4 display-1 mb-2", "type": "date", "style" : "border: none;"}), label="Fecha Termino Uso")