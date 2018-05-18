#usando tree de la libreria sklearn
from sklearn import tree

#importando las funciones que usamos en skcontabla
from skcontabla import lista_X,lista_Y


def predictor():
	
	#[peso min, peso max, altura][X lista de listas, en kg y mts]
	X = lista_X()
	#['Mujer','Hombre']
	Y = lista_Y()

	#clasificador clf
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X,Y)

	#medidas para evaluar
	prediccion = clf.predict([[84.9,89.1,2.6]])

	return prediccion
	

if __name__ == "__main__":
	print(predictor())
