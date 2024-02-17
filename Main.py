import random
list_anime=[]
anime_name= "None"
i = 0
print("Note: Type'done'for stoping input commands..")


while(anime_name != "done"):
  i=i+1
  anime_name = input(f"{i}. Enter name of any show: ")
  if(anime_name!="done"):
   list_anime.append(anime_name)
    

random_numb = random.randint(1,len(list_anime)-1)
print("You can watch ",list_anime[random_numb])
