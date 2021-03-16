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


* Most viwed products 



#2. Collaborative Filtering 

 Voor Collaborative Filtering heb ik de profiels naar types [BUYER , BOUNCER , BROWSERS] gefilterd waarbij elke van die profiels wordt gekijken naar welke prodducten worden gekocht en welke was als een recommendation, 

Na het Filtering worden verschillende tabellen gemaakt voor verschillende recommendations opbases van profiels types.  

  
*profiels types bouncer of browser 



*profiels type buyer
  