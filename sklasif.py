#usando tree de la libreria sklearn
from sklearn import tree

def predictor():
	
	#[altura, peso, talle][X lista de listas]
	X = [[181, 80, 44], [177, 70, 43], [160, 60, 38],
	 [154, 54, 37], [166, 64, 40], [190, 90 ,47],
	 [175, 64, 39], [177, 70, 40], [159, 75, 42],
	 [181, 85, 43]]

	Y = ['Hombre','Hombre','Mujer','Mujer','Mujer',
	'Hombre','Mujer','Mujer','Hombre','Hombre']

	#clasificador clf
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X,Y)

	#medidas para entrenar
	prediccion = clf.predict([[180,95,43]])

	return prediccion


if __name__ == "__main__":
	print(predictor())
