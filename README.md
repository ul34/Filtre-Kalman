# Filtre-Kalman-Complementaire


-Le bruit et le biais

Le bruit en electronique peut etre definit comme une quantite d'energie apporte a un systeme de maniere aleatoire en frequence et en amplitude ce bruit peut etre cause par la temperature, ondes electromagnetiques, impurete dans un semi conducteur,vibration...
Nous allons voir comment filtrer le bruit d'un gyroscope et d'un accelerometre on considerera que le bruit suis une distribution gaussienne. 


On dit que le gyroscope a un biais car nos mesures se font de maniere discrete, a chaque mesure du gyroscope en degres/S on concidere que la vitesse de deplacement et constante entre la derniere mesure et la prochaine mesure. Par exemple votre frequence de mesure est de 200HZ si vous mesurer 200°/S on concidere que le mobile c est deplace de 1°(0.005*200=1) mais ce n est pas totalement vrai car en realite pendant les 0.005S qu il c est ecouler rien ne vous dit que votre mobile se deplacer constament a 200°/S alors on peut deduire qua chaque mesure il ya une erreur qui se cumule.


-Le filtre de kalman

Le filtre de kalman est un filtre qui vous fournie une reponse fondee sur les entres et les valeurs anterieures de cette reponse (filtre a reponse impulsionnelle infinie) il permet d estimer l etat d un systeme dynamique en se basant sur une serie de mesure biaise et bruite.

Le filtre de kalman est separe en deux phases la premiere appelle prediction prend l etat a l instant T-1 pour produire l etat a linstant T la deuxieme phases est appele mise a jour utilisent les observations a linstant T pour corriger la prediction est donner un estimation plus precise.





<img src="https://raw.githubusercontent.com/ul34/Filtre-Kalman-Complementaire/master/%20FK.png" width="200" height="125">

 
 

<img src=" " width="200" height="125">
