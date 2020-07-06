# Filtre-Kalman


 -Le bruit et le biais

Le bruit en électronique peut être définit comme une quantité d’énergie apporte a un système de maniéré aléatoire en fréquence et en amplitude ce bruit peut être causé par la température, ondes électromagnétiques, impureté dans un semi conducteur,vibration...
Nous allons voir comment filtrer le bruit d'un gyroscope et d'un accéléromètre on considérera que le bruit suis une distribution gaussienne. 


On dit que le gyroscope a un biais car nos mesures se font de maniéré discrète, a chaque mesure du gyroscope en degrés/S on considéré que la vitesse de déplacement et constante entre la dernière mesure et la prochaine mesure. Par exemple votre fréquence de mesure est de 200HZ si vous mesurer 200°/S on considéré que le mobile c est déplace de 1°(0.005*200=1) mais ce n est pas totalement vrai car en réalité pendant les 0.005S qu il c’est écouler rien ne vous dit que votre mobile se déplacer constamment a 200°/S alors on peut déduire qua chaque mesure il ya une erreur qui se cumule.


-Le filtre de Kalman

Le filtre de Kalman est un filtre qui vous fournie une réponse fondée sur les entres et les valeurs antérieures de cette réponse (filtre a réponse impulsionnelle infinie) il permet d’estimer l état d un système dynamique en se basant sur une série de mesure biaise et bruite.

Le filtre de Kalman est sépare en deux phases la première appelle prédiction prend l’état a l instant T-1 pour produire l’état a l’instant T la deuxième phases est appelle mise a jour utilisent les observations a l’instant T pour corriger la prédiction est donner un estimation plus précise.
Prediction 









<img src="https://raw.githubusercontent.com/ul34/Filtre-Kalman-Complementaire/master/%20FK.png" width="700" height="700">

 
 

 

https://support.minitab.com/fr-fr/minitab/18/help-and-how-to/modeling-statistics/anova/supporting-topics/anova-statistics/what-is-the-variance-covariance-matrix/
