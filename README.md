# Filtre-Kalman-Complementaire


-Le bruit et le biais

Le bruit en electronique peut etre definit comme une quantite d'energie apporte a un systeme de maniere aleatoire en frequence et en amplitude ce bruit peut etre cause par la temperature, ondes electromagnetiques, impurete dans un semi conducteur,vibration...
Nous allons voir comment filtrer le bruit d'un gyroscope et d'un accelerometre on considerera que le bruit suis une distribution gaussienne. 


On dit que le gyroscope a un biais car nos mesures se font de maniere discrete, a chaque mesure du gyroscope en degres/S on concidere que la vitesse de deplacement et constante entre la derniere mesure et la prochaine mesure. Par exemple votre frequence de mesure est de 200HZ si vous mesurer 200°/S on concidere que le mobile c est deplace de 1°(0.005*200=1) mais ce n est pas totalement vrai car en realite pendant les 0.005S qu il c est ecouler rien ne vous dit que votre mobile se deplacer constament a 200°/S alors on peut deduire qua chaque mesure il ya une erreur qui se cumule.



<img src=" " width="200" height="125">

 
 

<img src=" " width="200" height="125">
