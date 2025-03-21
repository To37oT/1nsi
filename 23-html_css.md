---
layout: default
title: Chapitre 23 - HTML et CSS
permalink: /chapitre23/
published: true
date: 2024
---

# HTML et CSS

## 1) introduction

Nous allons nous intéresser à un acteur fondamental du développement web, le couple **HTML + CSS** (Hyper Text Markup Langage et Cascading Style Sheets).

## 2) le HTML

Le HTML (HyperText Markup Language), est le format de données conçu pour représenter les pages web. C’est un **langage de balisage** (avec des balises). HTML permet de structurer **sémantiquement** et de mettre en forme le contenu des pages, d’inclure du texte, des images, des formulaires de saisie... Il est souvent utilisé avec des langages de programmation (JavaScript) et des formats de présentation (CSS).

C'est votre **navigateur** (Firefox, Chrome, Opera,....) qui s'occupera de lire le HTML et d'afficher les éléments (texte, images, videos...).

**HTML n'est pas un langage de programmation** (comme le Python par exemple), ici, pas question de conditions, de boucles....c'est **un langage de description**.

Voici un exemple de code HTML :

```html
<h1>Hello World! Ceci est un titre</h1>
<p>Ceci est un <strong>paragraphe</strong>. Avez-vous bien compris ?</p>
```

En HTML tout est une histoire de balise que l'on ouvre et que l'on ferme. Une **balise ouvrante** est de la forme ```<nom_de_la_balise>```, les **balises fermantes** sont de la forme ```</nom_de_la_balise>```.

En observant attentivement le code, vous devriez forcément remarquer que toute balise ouverte doit être refermée à un moment ou un autre. La balise ouvrante et la balise fermante peuvent être sur la même ligne ou pas, cela n'a aucune importance, la seule question à se poser ici est : **ai-je bien refermé toutes les balises que j'ai ouvertes ?**

Enfin pour terminer avec les généralités sur les balises, il est important de savoir qu'une structure de ce type est interdite :

```
<balise1>
<balise2>
</balise1>
</balise2>
```

La balise2 a été ouverte **après** la balise1, elle devra donc être refermée **avant** la balise1.

En revanche, l'enchaînement suivant est correct :

```
<balise1>
<balise2>
</balise2>
</balise1>
```

Nous ajouterons même une identition, non obligatoire mais qui permet une meilleure lisibilité du code.

```
<balise1>
	<balise2>
	</balise2>
</balise1>
```

Notez que dans notre exemple nous respectons bien cette règle « d'imbrication » des balises avec la balise ```<p>``` et la balise ```<strong>```.

### A. La sémantique

Il est important de comprendre que chaque balise a une signification qu'il faut bien respecter (on parle de la sémantique des balises, son "**sens**"). Par exemple le texte situé entre la balise ouvrante et fermante ```<h1>``` est obligatoirement un titre important (il existe des balises ```<h2>```, ```<h3>```......qui sont aussi des titres, mais des titres moins importants (sous-titre)). 

La balise ```<p>``` permet de définir des paragraphes, enfin, la balise ```<strong>``` permet de mettre en évidence un élément important.

La sémantique est importante à respecter, elle aide votre navigateur à comprendre le sens de votre page et renforce la visibilité de votre site dans les résultats des moteurs de recherche.


### B. Les attributs

Il est possible d'ajouter des éléments à une balise ouvrante, on parle d'attribut. Une balise peut contenir plusieurs attributs :

```html
<ma_balise attribut_1="valeur_1" attribut_2="valeur_2">
```

Il existe beaucoup d'attributs différents, nous allons nous contenter de 2 exemples avec l'attribut id (id pour identifiant) et class. Nous verrons l’intérêt de ces attributs prochainement

```html
<h1>Ceci est un titre</h1>
<h2 class="titre_1">Ceci est un sous titre</h2>
<p id="para_1">Ceci est un <strong>paragraphe</strong>. Avez-vous bien compris ?</p>
```

### C. Les balises orphelines

Il  existe  une  exception  concernant  l'imbrication  des  balises,  quelques  rares  balises  s'ouvrent, mais ne se ferme pas (comme la balise permettant de mettre une image).

## 3) Le CSS

Le HTML n'a pas été conçu pour gérer la mise en page. Le HTML s'occupe uniquement du contenu et de la sémantique, pour tout ce qui concerne la mise en page et l'aspect décoratif (on parle du style de la page), on utilisera le CSS (Cascading Style Sheets).

Voici un exemple de code CSS :

```css
h1
{
	text-align: center;
	background-color: red;
}

h2
{
	font-family: Verdana;
	font-style: italic;
	color: green;
}
```

Dans l'exemple ci-dessus, les propriétés *text-align* (permet de choisir l'alignement d'un texte) et *background-color* (permet de modifier la couleur de fond) seront appliquées au contenu **de toutes les balises de type h1** (avec respectivement les valeurs *center* et *red* : les textes contenus dans les balises *h1* seront centrés et la couleur de fond sera rouge).

Le contenu des balises *h2* sera écrit avec la police de caractère *Verdana*, en italique et en vert.

Si on désire cibler seulement certaines balises et pas les autres, il est possible d'utiliser les attributs *id* et *class*:

voici du code HTML :

```html
<h1>Ceci est un titre</h1>
<p>Bonjour</p>
<p id="para_1">Vous allez bien ?</p>
```

et le code CSS correspondant :

```css
#para_1
{
	font-style: italic;
	color: green;
}
```

Ici seul le second paragraphe (*Vous allez bien ?*) sera concerné par le CSS ci-dessus. Le premier paragraphe (*Bonjour*) et le titre *h1* ne seront pas concernés

Il est donc possible de cibler un paragraphe et pas un autre en utilisant l'id du paragraphe (**en CSS l'id se traduisant par le signe #**).

Il est aussi possible d'utiliser l'attribut class à la place de l'id. **Dans le CSS on utilisera le point . à la place du #**.

> Nous ne nous attarderons pas sur la différence entre id et class, sachez juste qu'un même id est unique dans chaque page web alors qu'une classe peut-être utilisée plusieurs fois dans la même page.
> 
> L'attribut class permet de donner le même nom à plusieurs reprises dans une même page, ce qui n'est pas possible avec l'attribut *id*
> 
> Si nous avions eu un 3e paragraphe, nous aurions pu avoir : ```<p class="para_1">Voici un 3e paragraphe</p>```, mais nous n'aurions pas pu avoir : ```<p id="para_1"> Voici un 3e paragraphe </p>```, car le nom para_1 a déjà été utilisé pour le 1er paragraphe.

## 4) Quelques balises à connaître

### a) La balise *a*

La balise *a* permet de créer des liens hypertextes, ce sont ces liens hypertextes qui vous permettent de naviguer entre les pages d'un site ou entre les sites. Les liens hypertextes sont par défaut soulignés et de couleur bleue (modifiable grâce au CSS). La balise *a* possède un attribut *href* qui a pour valeur le chemin du fichier que l'on cherche à atteindre ou l'adresse du site cible : 

```html
<a href="https://www.sfda37.fr/">Cliquez ici</a>
```

Entre la balise ouvrante et fermante, on trouve le texte qui s'affichera à l'écran (c'est ce texte qui est souligné et de couleur bleue). La balise peut sans problème se trouver en plein milieu d'un paragraphe.

### b) La balise *image*

La balise image sert à insérer des images :

```html
<img src="mon_image.jpg" alt="avion">
```

La balise img ne se ferme pas. Elle possède 2 attributs importants :

- **src** qui doit être égal au nom du fichier image (ou au chemin, relatif ou absolu, si le fichier image se trouve dans un autre dossier).
- **alt** qui doit être égal à une description de votre image, il faut systématiquement renseigner cet attribut.

### c) les balises form, label, input et button

Les formulaires sont des éléments importants des sites internet, ils permettent à l'utilisateur de transmettre des informations. Un formulaire devra être délimité par une balise form :

```
<form>
....
</form>
```

Il existe différentes balises permettant de construire un formulaire, notamment la balise *input*. Cette balise possède un attribut type qui lui permet de jouer des rôles très différents.

Les balises *button* et *label* nous seront aussi d'une grande utilité  :

```html
<form>
	<label>voici un champ de texte : </label>
	<input type="text">
	<button>Cliquez ici !</button>
</form>
```

### d) les balises *div* et *span*

Ces 2 balises sont très utilisées (surtout la balise div). Pourtant, il faudrait, autant que possible, les éviter, pourquoi ?

Parce qu'elles n'ont aucune signification particulière, ce sont des balises dites “génériques”.

À quoi servent-elles alors ?

À organiser la page, à regrouper plusieurs balises dans une même entité :

```html
<div>
	<h2> Mon en-tête </h2>
	<p>Hello, comment ça va ?</p>
</div>
<div>
	<h2>mon <span>bas</span> de page</h2>
	<p>Au  revoir !</p>
</div>
```

Pourquoi 2 balises génériques ?

Parce que div est une balise de type “block” et que span est une balise de type “inline” (voir partie suivante).

Aujourd'hui pour remplacer la balise div, nous avons plusieurs balises qui font exactement la même chose, mais ajoute également un peu de sens au regroupement : 

```html
<header></header>
<nav></nav>
<main></main>
<section></section>
<article></article>
<footer></footer>
<aside></aside>
```

## 5) les balises de type *block* et les balises de type *inline*

Sans trop entrer dans les détails, il faut bien comprendre que l'ordre des balises dans le code HTML a une grande importance. Les balises sont affichées les unes après les autres, on parle du **flux** normal de la page.

C'est ici qu'entrent en jeu les balises de type "block" et les balises de type "inline".

Les contenus des balises de type "block" (p, div,h1,...) se placent sur la page web les uns en dessous des autres.

Les contenus des balises de type "inline" (strong, img, span, a) se placent sur la page web les uns à côté des autres.

Cela revient à dire qu'une balise de type “block” prend toute la largeur de la page alors qu'une balise de type “inline” prend juste la largeur qui lui est nécessaire.

## 6) écrire une page HTML

Pour écriture une page HTML complète, il est nécessaire de rajouter quelques balises :

```html
<!doctype html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<title>Voici mon site</title>
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		
	</body>
</html>
```

Nous n'allons pas nous attarder sur ce squelette de page HTML, mais voici ce que vous devez savoir :

- la première ligne (```<!doctype html>```) permet d'indiquer au navigateur que nous utiliserons du HTML

- la balise *html* est obligatoire, l'attribut lang="fr" permet d'indiquer au navigateur que nous utiliserons le français pour écrire notre page.

- la balise *head* délimite ce que l'on appelle l'en-tête. L'en-tête contient, dans notre exemple, 3 balises : 
	- la balise *meta* possède l'attribut *charset="utf-8* qui permet de définir l'encodage des caractères (ici utf-8)
	
	- la balise *title* qui définit le titre de la page (titre qui s'affiche dans l'onglet du navigateur)
	
	- la balise *link va permettre de relier votre HTML et votre CSS. Votre CSS se trouvera dans un fichier indépendant (ici *style.css*), l'attribut *href* correspond au chemin (relatif ou absolu) vers ce fichier

- toutes les balises qui composeront votre page (p, h1, img...) **devront se trouver** entre la balise *body* ouvrante et la balise *body* fermante.

Pour créer une nouvelle page, il suffira de copier-coller ce squelette de page HTML dans un nouveau fichier et de le compléter avec votre code HTML (entre les balises *body*) 
