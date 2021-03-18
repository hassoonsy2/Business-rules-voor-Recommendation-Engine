# Business-rules-voor-Recommendation-Engine

Naam : Hussin Almoustafa 

Studentnr : 1776495 

Klas : gp-v1a 


#Business-rules : 

#1 . Content-Based Filtering 

 Voor content filtering heb ik als eerst de meest verkochte producten geselecteerd uit onder andere de tabel Orders. Deze tabel bevat informatie zoals (product.id, profiel.id).                   
        Met inner join kon in nog meer informatie over de producten selecteren, zoals (product.name) uit de tabel products. Om dit allemaal om te zetten in een recommendation, is er een nieuwe tabel    
        genaamd (Best_Seller). Deze tabel bevat informatie over welke producten het meest verkocht worden en hoe vaak. 

* Most sold products 


![bestseller](https://user-images.githubusercontent.com/71430169/111646807-41c9fa00-8802-11eb-9816-8761731cd605.PNG)
 


* Most viwed products 


![mostviwedpro](https://user-images.githubusercontent.com/71430169/111646882-527a7000-8802-11eb-9b2c-d559986e5140.PNG)




#2 . Collaborative Filtering 

 Voor Collaborative Filtering heb ik de profiels naar types [BUYER , BOUNCER , BROWSERS] gefilterd waarbij elke van die profiels wordt gekijken naar welke prodducten worden gekocht en welke was als een recommendation, 

Na het Filtering worden verschillende tabellen gemaakt voor verschillende recommendations opbases van profiels types.  

  

*profiels types bouncer of browser 

BOUNCER :

![bouncer](https://user-images.githubusercontent.com/71430169/111646952-602ff580-8802-11eb-8ef9-89021a1ce5ad.PNG)




BROWSER : 

![browser](https://user-images.githubusercontent.com/71430169/111647002-6a51f400-8802-11eb-978d-72de128bbc68.PNG)





*profiels type buyer


![buyer](https://user-images.githubusercontent.com/71430169/111647089-7a69d380-8802-11eb-949c-a29994258e4f.PNG)

  