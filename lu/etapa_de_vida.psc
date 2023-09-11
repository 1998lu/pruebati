Algoritmo etapa_de_vida
	//programa que devuekve l ETAPA DE VIDA DE UNA PERSONA SEGUN SU EDAD
	DEFINIR EDADPERSONA Como Entero
	ESCRIBIR "INGRESE LA EDAD DE LA PERSONA"
	LEER EDADPERSONA
	SI EDADPERSONA > 0 Y EDADPERSONA <=2
		ESCRIBIR "La persona es un bebe"
	SiNo
		si EDADPERSONA > 2 y EDADPERSONA <= 11
			escribir "la persona es un niño"
		SiNo
			si EDADPERSONA > 11 y EDADPERSONA <= 13
				Escribir "la persona es puberto"
			sino 
				si EDADPERSONA > 13 y EDADPERSONA <= 18
					escribir "es un adolescente"
				SiNo
					si EDADPERSONA>18 y EDADPERSONA <= 28
						escribir "la persona es joven aun"
					sino
						si EDADPERSONA > 28
							escribir "es adulto"
						FinSi
						
						
					FinSi
			FinSi
		FinSi
	FinSi
	FinSi

FinAlgoritmo
