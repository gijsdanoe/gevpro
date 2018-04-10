### acc_haiku.py ###
by Thomas Tan, Jan Harms, Gijs Danoe, Inge Salomons


### Information about the program ###
When running the program acc_haiku.py (without arguments) in Python3,
the program randomly picks a tweet from a database of Dutch tweets from
2011 until 2018 and checks if the tweet meets the requirements.
These requirements are: consisting of only words that are in the CELEX database;
consisting of exactly 17 syllables and having the haiku structure of 5-7-5 syllables.
If a tweet meets the requirements, the program prints it in haiku form and automatically
tweets the haiku on the Twitter account 'HaikuPerOngeluk' along with the name of the user of the tweet.
If a tweet does not meet the requirements, the program randomly picks another tweet,
until a tweet is found that does.


### Logboek ###
Wanneer:    Hoelang:    Wat:                                                        Wie:
07-3-2018   2 uur       Team en repository Bitbucket aanmaken en lokaal klonen      Jan, Thomas, Gijs, Inge
12-3-2018   1 uur       Overleggen over functies                                    Jan, Thomas, Gijs, Inge
12-3-2018   1 uur       main() schrijven en tokenize() toevoegen                    Inge
12-3-2018   1,5 uur     main() schrijven                                            Jan en Inge
12-3-2018   3 uur       sylcount.py schrijven                                       Gijs, Thomas, Jan
19-3-2018   2 uur       Main() aanpassen                                            Inge, Jan
19-3-2018   2 uur       sylcount.py schrijven                                       Gijs
20-3-2018   1 uur       Overleggen over main()                                      Jan, Thomas, Inge
20-3-2018   0,5 uur     count_check() schrijven en main() aanpassen                 Inge
20-3-2018   0,5 uur     haiku_check() schrijven                                     Jan
20-3-2018   0,5 uur     generate_haiku(0 schrijven                                  Thomas
20-3-2018   3 uur       sylcount.py schrijven                                       Gijs
20-3-2018   1,5 uur     Functies testen en debuggen                                 Jan, Thomas, Inge
28-3-2018   2 uur       Functies testen en debuggen, make_dict.py schrijven 
...                         en dpw.p aanmaken                                       Jan, Thomas, Inge, Gijs
03-4-2018   4 uur       Functies testen en debuggen, sylcount.py in make_dict.py
...                         integreren en nieuwe dwp.p aanmaken                     Jan, Thomas, Gijs
04-4-2018   4 uur       Programma afmaken, twitterbot realizeren,
...                         tokenize() in main() integreren                         Jan, Thomas, Gijs, Inge
05-4-2018   3 uur       pep8 en pycodestyle toepassen, comments toevoegen, info
...                         in README.md schrijven, detokenizer toevoegen           Inge
10-4-2018   2 uur       Checken of alles goed werkt en inleveren                    Jan en Inge