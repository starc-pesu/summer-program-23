import math
import numpy as np
import pickle
import streamlit as st
import emoji
import folium
from streamlit_folium import st_folium
from streamlit_extras.colored_header import colored_header

# st.set_page_config(page_title='IPL_Score_Predictor',layout="wide")


tab1, tab2 ,tab3,tab4, tab5, tab6, tab7, tab8, tab9, tab10,  tab11,  tab12,  tab13,  tab14,  tab15,  tab16 = st.tabs(["2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008"])


with tab1:
    st.title('IPL-2023')

    st.image('https://ss-i.thgim.com/public/incoming/htd7c/article66909875.ece/alternates/FREE_1200/RON_1392.JPG',width=600)
    st.caption('Champions-Chennai Super Kings')

    st.write('Orange Cap-Shubman Gill')
    st.write('Purple Cap winner-Mohammed Shami')
    st.write('Man of the tournament-Shubman Gill')
    st.write('Fair Play Award-Delhi Capitals')
    st.write('Emerging Player-Yashasvi Jaiswal')
    st.caption("The 2023 Indian Premier League (also known as Tata IPL 2023 for sponsorship reasons and sometimes referred to as IPL 2023 or IPL 16) was the 16th season of the Indian Premier League, a franchise Twenty20 cricket league in India. It is organised by the Board of Control for Cricket in India.[1]In the final, Chennai Super Kings defeated Gujarat Titans, by five wickets (DLS method) to win their record fifth league title.")
    st.caption('The league returned to its original home-and-away format after a period of four years.Due to the COVID-19 pandemic, the previous three seasons were held at neutral venues.Fan parks were organised in 45 cities, events which last occurred in 2019,and an opening ceremony took place for the first time with performances from Arijit Singh, Tamannaah Bhatia, and Rashmika Mandanna.')
    st.caption('A number of new laws/rules have been introduced in this season:A penalty of five runs if unfair movement by a fielder or wicketkeeper occurs as a ball being delivered and before it is received by the batsman. The dead ball will also be declared.Teams can be declared after the toss.An Impact Player rule allowing sides to substitute a player during a match from four named substitutes.If a team fails to bowl their 20 overs in the allocated time, only four fielders will be allowed outside of the fielding restrictions circle for the remainder of the innings.Teams can review balls for wides and no-balls using the Decision Review System (DRS). This change was first used during the 2023 Women Premier League.')
    st.markdown("---")


with tab2:
    st.title('IPL-2022')
    st.image('https://m.economictimes.com/thumb/msid-91886579,width-1600,height-984,resizemode-4,imgsize-445454/gujarat-titans-players-with-the-ipl-trophy.jpg',width=600)
    st.caption('Champions-Gujarat Titans')
    st.write('Orange Cap-Jos Buttler')
    st.write('Purple Cap winner-Yuzuvendra Chahal')
    st.write('Man of the tournament-Jos Buttler')
    st.write('Fair Play Award-Rajasthan Royals')
    st.write('Emerging Player-Umran Malik')
    st.caption('The 2022 Indian Premier League, also known as IPL 15 or for sponsorship reasons, TATA IPL 2022, was the fifteenth season of the Indian Premier League (IPL), a professional Twenty20 cricket league established by the Board of Control for Cricket in India (BCCI) in 2007. The tournament was played from 26 March 2022 to 29 May 2022. The group stage of the tournament was played entirely in the state of Maharashtra, with Mumbai, Navi Mumbai and Pune hosting matches.[3][4]The season saw the expansion of the league with the addition of two new franchises.Chennai Super Kings were the defending champions, having won their fourth title during the previous season.[8]In the final, Gujarat Titans beat Rajasthan Royals, by seven wickets to win their maiden title in their very first season.')
    st.caption('Each existing team was allowed to retain a maximum of four players, with the two new teams were allowed to select a maximum of three players before the auction.The retained players of the existing eight teams were announced on 30 November 2021,and the two new teams named their selections on 22 January 2022.The player auction to complete team squads took place on 12 and 13 February 2022 in Bangalore.Ishan Kishan was the most expensive buy of the auction, bought by Mumbai Indians for ₹15.25 crore (US$1.9 million).[31] The most expensive overseas player was Liam Livingstone.')
    st.caption('A number of new laws/rules have been introduced in this season:A penalty of five runs if unfair movement by a fielder or wicketkeeper occurs as a ball being delivered and before it is received by the batsman. The dead ball will also be declared.Teams can be declared after the toss.An Impact Player rule allowing sides to substitute a player during a match from four named substitutes.If a team fails to bowl their 20 overs in the allocated time, only four fielders will be allowed outside of the fielding restrictions circle for the remainder of the innings.Teams can review balls for wides and no-balls using the Decision Review System (DRS). This change was first used during the 2023 Women Premier League.')
    
    st.markdown('---')


with tab3:
    st.title('IPL-2021')
    st.image('https://images.thequint.com/thequint%2F2021-10%2Fd985b5d5-8851-4d3c-91ab-5b9654819ffc%2FRON_4513__1_.JPG?auto=format%2Ccompress&fmt=webp&width=720&w=1200',width=600)
    st.caption('Champions-Chennai Super Kings')
    st.write('Orange Cap-Ruturaj Gaikwad')
    st.write('Purple Cap winner-Harshal Patel')
    st.write('Man of the tournament-Harshal Patel')
    st.write('Fair Play Award-Rajasthan Royals')
    st.write('Emerging Player-Ruturaj Gaikwad')
    st.caption('IPL 2021, the 14th edition of the Indian Premier League, began on April 9 and was scheduled to run until May 30, featuring eight teams competing in a double round-robin format across six venues in India. The tournament witnessed electrifying matches and exceptional performances from players. Before its suspension on May 4 due to the escalating COVID-19 pandemic, the Delhi Capitals led the points table with 12 points, with standout performances from Shikhar Dhawan as the leading run-scorer and Harshal Patel as the highest wicket-taker. Efforts to reschedule the remaining matches in September 2021 were discussed but ultimately abandoned due to logistical constraints.')
    st.caption('Following the suspension of IPL 2021, the tournament faced challenges in rescheduling the remaining matches. Various factors such as the international cricket calendar, player availability, and venue logistics posed obstacles to finding a suitable window to complete the tournament. Despite discussions and deliberations, it was eventually decided that IPL 2021 would not resume in 2021, and the remaining matches would be held at a later date. This marked an unprecedented interruption in the history of the IPL, highlighting the impact of the global pandemic on sporting events worldwide. The BCCI and IPL governing council remained committed to prioritizing the safety and well-being of players, staff, and stakeholders, making the decision to suspend and postpone the tournament in the best interest of all involved. IPL fans eagerly awaited updates on the rescheduling of the remaining matches, while the cricketing fraternity acknowledged the challenges faced and hoped for a successful completion of the tournament in the future.')
    
    st.markdown('---')


with tab4:
    st.title('IPL-2020')
    st.image('https://img.olympicchannel.com/images/image/private/t_social_share_thumb/f_auto/primary/u4vjp5xs7mbfm2hyesv5',width=600)
    st.caption('Champions-Mumbai Indians')
    st.write('Orange Cap-KL Rahul')
    st.write('Purple Cap winner-Kagiso Rabada')
    st.write('Man of the tournament-Jofra Archer')
    st.write('Fair Play Award-Mumbai Indians')
    st.write('Emerging Player-Devdutt Padikkal')
    st.caption('IPL 2020, the 13th edition of the Indian Premier League, was a tournament filled with excitement and challenges due to the global COVID-19 pandemic. Originally scheduled to be held from March 29 to May 24, 2020, in India, the tournament was postponed and later relocated to the United Arab Emirates (UAE) due to the rising number of COVID-19 cases in India. The matches were played across three venues in the UAE: Dubai, Abu Dhabi, and Sharjah. Eight teams competed in a double round-robin format, followed by playoffs. Mumbai Indians emerged as the champions for the fifth time in IPL history, defeating the Delhi Capitals in the final. The tournament witnessed exceptional performances from players like KL Rahul, who won the Orange Cap for being the leading run-scorer, and Kagiso Rabada, who claimed the Purple Cap for being the highest wicket-taker. The bio-secure bubble and strict protocols were put in place to ensure the safety of players and staff, allowing the tournament to be completed successfully despite the challenges posed by the pandemic. IPL 2020 served as a symbol of resilience and provided cricket fans with a much-needed source of entertainment during these uncertain times.')
    st.caption('In addition to the challenges posed by the pandemic, IPL 2020 also witnessed some memorable moments and records. The tournament showcased several nail-biting encounters, thrilling last-over finishes, and outstanding individual performances. It was a season of comebacks, with players like Suryakumar Yadav, Ishan Kishan, and T. Natarajan making a mark with their consistent performances. Rahul Tewatias incredible innings, where he smashed five sixes in an over, will be remembered as one of the most extraordinary comebacks in IPL history. The emergence of young talents like Devdutt Padikkal, Ruturaj Gaikwad, and Kartik Tyagi highlighted the nurturing ground IPL provides for budding cricketers. The Mumbai Indians displayed their dominance throughout the tournament, clinching the title with a comprehensive victory in the final. IPL 2020 demonstrated the resilience of the sport and its ability to bring joy and unity to millions of fans, serving as a beacon of hope during a challenging year.')
    
    st.markdown('---')         

with tab5:
    st.title('IPL-2019')
    st.image('https://i.ytimg.com/vi/MKqwLzYTDlE/maxresdefault.jpg',width=600)
    st.caption('Champions-Mumbai Indians')
    st.write('Orange Cap-David Warner')
    st.write('Purple Cap winner-Imran Tahir')
    st.write('Man of the tournament- Andre Russell')
    st.write('Fair Play Award-Sunrisers Hyderabad')
    st.write('Emerging Player-Shubman Gill')
    st.caption('IPL 2019, the 12th edition of the Indian Premier League, was a captivating tournament that showcased thrilling cricketing action and captivating performances. Held from March 23 to May 12, 2019, the tournament featured eight teams competing in a double round-robin format followed by playoffs. Mumbai Indians emerged as the champions for the fourth time in IPL history, defeating the Chennai Super Kings in a tense final. Throughout the season, there were exceptional individual displays, with Andre Russell of the Kolkata Knight Riders standing out as a force to be reckoned with, displaying his immense power-hitting abilities. David Warner of the Sunrisers Hyderabad reclaimed the Orange Cap as the leading run-scorer, while Imran Tahir of the Chennai Super Kings claimed the Purple Cap as the highest wicket-taker. The tournament witnessed close finishes, incredible comebacks, and intense rivalries, captivating fans worldwide. IPL 2019 was a testament to the popularity, showcasing the high-quality cricket and entertainment it offers year after year.')
    st.caption('In addition to the thrilling on-field action, IPL 2019 had its fair share of controversies and dramatic moments. One of the notable incidents was the Mankad controversy involving Ravichandran Ashwin of the Kings XI Punjab, who ran out Jos Buttler of the Rajasthan Royals at the opposite end. This incident sparked intense debates and discussions on the spirit of the game. Another significant controversy involved the no-ball controversy during a match between Royal Challengers Bangalore and Mumbai Indians, where an umpiring error led to a missed no-ball call that could have potentially changed the outcome of the match. Despite these controversies, the tournament continued to captivate fans with close matches, outstanding performances, and intense rivalries. The rise of young talents like Prithvi Shaw, Shubman Gill, and Riyan Parag showcased the depth of talent in Indian cricket. IPL 2019 further solidified its position as one of the premier T20 leagues in the world, attracting top players from across the globe and providing a platform for budding cricketers to shine on the big stage. It was a season filled with excitement, drama, and unforgettable moments, leaving fans eagerly awaiting the next edition of the IPL.')
    st.caption('In addition to the challenges posed by the pandemic, IPL 2020 also witnessed some memorable moments and records. The tournament showcased several nail-biting encounters, thrilling last-over finishes, and outstanding individual performances. It was a season of comebacks, with players like Suryakumar Yadav, Ishan Kishan, and T. Natarajan making a mark with their consistent performances. Rahul Tewatias incredible innings, where he smashed five sixes in an over, will be remembered as one of the most extraordinary comebacks in IPL history. The emergence of young talents like Devdutt Padikkal, Ruturaj Gaikwad, and Kartik Tyagi highlighted the nurturing ground IPL provides for budding cricketers. The Mumbai Indians displayed their dominance throughout the tournament, clinching the title with a comprehensive victory in the final. IPL 2020 demonstrated the resilience of the sport and its ability to bring joy and unity to millions of fans, serving as a beacon of hope during a challenging year.')
    
    st.markdown('---')    

with tab6:
    st.title('IPL-2018')
    st.image('https://akm-img-a-in.tosshub.com/indiatoday/images/breaking_news/201805/DeOZXURVMAAHJrA.jpg_large.jpeg?VersionId=DvXS7HI0un1tvS_tQWpzD7noPfNDc0wm',width=600)
    st.caption('Champions-Chennai Super Kings')
    st.write('Orange Cap- Kane Williamson ')
    st.write('Purple Cap winner-Imran Tahir')
    st.write('Man of the tournament- Sunil Narine')
    st.write('Fair Play Award-Mumbai Indians')
    st.write('Emerging Player-Rishabh Pant')
    st.caption('IPL 2018, the 11th edition of the Indian Premier League, was a riveting tournament filled with high-intensity cricket and remarkable performances. Spanning from April 7 to May 27, 2018, the season featured eight teams competing in a double round-robin format followed by playoffs. The Chennai Super Kings made a triumphant return after a two-year suspension, clinching the title for the third time. The final, held at the Wankhede Stadium in Mumbai, saw an enthralling showdown between the Chennai Super Kings and the Sunrisers Hyderabad, with Shane Watsons scintillating century leading Chennai to victory. Throughout the tournament, individual brilliance was on full display, with Kane Williamson of the Sunrisers Hyderabad emerging as the leading run-scorer and Andrew Tye of the Kings XI Punjab claiming the Purple Cap as the highest wicket-taker. IPL 2018 witnessed some memorable moments, such as AB de Villiers breathtaking innings against the Delhi Daredevils and the nail-biting finishes that became a hallmark of the tournament. The season showcased the fierce competition, emerging talents, and the enthralling atmosphere that have made the IPL one of the most popular cricket leagues in the world.')
    st.caption('In addition to the thrilling cricketing action, IPL 2018 also witnessed some notable controversies and memorable incidents. One of the major controversies surrounded the ball-tampering scandal involving the then-captain of the Rajasthan Royals, Steve Smith, and his teammate, Cameron Bancroft. Both players were suspended by Cricket Australia, and Smith stepped down as captain of the Royals. The incident generated widespread criticism and discussions on fair play and the integrity of the game. On a lighter note, the season saw some incredible individual performances, including Rashid Khans stunning all-round display for the Sunrisers Hyderabad and Rishabh Pants explosive batting for the Delhi Daredevils. Emerging talents like Mayank Markande, Prithvi Shaw, and Shubman Gill showcased their potential, adding to the excitement of the tournament. IPL 2018 also highlighted the importance of teamwork, as several teams relied on collective efforts rather than depending solely on individual brilliance. The season entertained fans with its electrifying matches, intense rivalries, and pulsating finishes, solidifying the reputation as a premier T20 league.')
    
    st.markdown('---')



with tab7:
    st.title('IPL-2017')
    st.image('https://resize.indiatvnews.com/en/resize/newbucket/1200_-/2020/05/pjimage-2020-05-21t221828-1590079713.jpg',width=600)
    st.caption('Champions-Mumbai Indians')
    st.write('Orange Cap winner- David Warner')
    st.write('Purple Cap winner-Bhuvneshwar Kumar')
    st.write('Man of the tournament-Ben Stokes ')
    st.write('Fair Play Award-Gujarat Lions ')
    st.write('Emerging Player-Basil Thampi')
    st.caption('IPL 2017, the 10th edition of the Indian Premier League, was a memorable tournament filled with thrilling cricketing action and remarkable performances. Held from April 5 to May 21, 2017, the season featured eight teams competing in a double round-robin format followed by playoffs. The Mumbai Indians emerged as champions for the third time in IPL history, defeating the Rising Pune Supergiant in a tense final. The final, held at the Rajiv Gandhi International Stadium in Hyderabad, witnessed an exhilarating battle between the two Maharashtra-based teams. Throughout the tournament, individual brilliance was on display, with David Warner of the Sunrisers Hyderabad emerging as the leading run-scorer, while Bhuvneshwar Kumar, also from the Sunrisers Hyderabad, claimed the Purple Cap as the highest wicket-taker. IPL 2017 was notable for some incredible performances, including Chris Lynns explosive batting for the Kolkata Knight Riders and Rashid Khans impressive bowling for the Sunrisers Hyderabad. The tournament also witnessed some close finishes, intense rivalries, and record-breaking moments, adding to the excitement and entertainment value of the league. IPL 2017 further solidified the leagues position as one of the premier T20 competitions in the world, captivating fans with its high-quality cricket and engaging atmosphere.')
    st.caption('In addition to the thrilling on-field action, IPL 2017 had its fair share of controversies and notable incidents. One of the major controversies surrounded the removal of the Rising Pune Supergiant and the Gujarat Lions from the IPL after the season, as the Board of Control for Cricket in India (BCCI) decided to revert to an eight-team format from the following edition. This decision raised concerns among the players and fans of the two franchises, leading to debates about the future of the teams and the impact on careers. On a positive note, IPL 2017 witnessed the rise of young talents like Rishabh Pant, Basil Thampi, and Rahul Tripathi, who made their mark with impressive performances and caught the attention of cricket enthusiasts. The tournament also marked the return of the prodigal son, MS Dhoni, as the captain of the Rising Pune Supergiant, creating a buzz among fans and adding to the overall excitement of the season. IPL 2017 further showcased the growing popularity of the league, with packed stadiums, massive television viewership, and increased fan engagement across various platforms. The tournament continued to provide a platform for established stars, emerging talents, and international players to showcase their skills, making it a celebrated event in the cricketing calendar.')
    
    st.markdown('---')         

with tab8:
    st.title('IPL-2016')
    st.image('https://www.100mbsports.com/wp-content/uploads/2020/08/SRH-e1598517915438.jpeg',width=600)
    st.caption('Champions-Sunrisers Hyderabad')
    st.write('Orange Cap winner- Virat Kohli')
    st.write('Purple Cap winner-Bhuvneshwar Kumar')
    st.write('Man of the tournament-Virat Kohli')
    st.write('Fair Play Award-Sunrisers Hyderabad')
    st.write('Emerging Player-Mustafizur Rahman')
    st.caption('IPL 2016, the ninth edition of the Indian Premier League, was a captivating tournament that showcased exceptional cricketing skills and memorable moments. Spanning from April 9 to May 29, 2016, the season featured eight teams competing in a double round-robin format followed by playoffs. The Sunrisers Hyderabad emerged as champions for the first time in IPL history, defeating the Royal Challengers Bangalore in a thrilling final. The final, held at the M. Chinnaswamy Stadium in Bengaluru, witnessed an intense battle between the two teams. Throughout the tournament, there were outstanding individual performances, with Virat Kohli of the Royal Challengers Bangalore leading the run charts and Bhuvneshwar Kumar of the Sunrisers Hyderabad claiming the Purple Cap for the highest wicket-taker. IPL 2016 witnessed some breathtaking moments, such as Kohlis extraordinary consistency with the bat, scoring four centuries in a single season, and the emergence of young talents like Mustafizur Rahman, who made a significant impact with his deceptive left-arm pace bowling. The tournament also had its share of controversies, including the suspension of two teams, Chennai Super Kings and Rajasthan Royals, due to their involvement in a spot-fixing scandal. Overall, IPL 2016 provided fans with thrilling cricketing action, intense rivalries, and a glimpse of the future stars of the game, solidifying its status as one of the most exciting T20 leagues in the world.')
    st.caption('In addition to the thrilling cricketing action, IPL 2016 witnessed several notable incidents and milestones. One of the highlights was the rise of young Indian talents, such as Rishabh Pant, Krunal Pandya, and Deepak Hooda, who showcased their skills and made significant contributions to their respective teams. Another remarkable moment came when Chris Gayle of the Royal Challengers Bangalore set a new record for the fastest century in IPL history, scoring 100 runs off just 30 balls against the Pune Warriors. The tournament also witnessed the retirement of one of the all-time greats, Shane Watson, who bid farewell to competitive cricket at the end of the season. Off the field, IPL 2016 continued its tradition of glitz and glamour, with Bollywood stars and international celebrities adding to the entertainment factor. The league also attracted massive crowds, with stadiums packed to the brim, and recorded high television viewership, further solidifying its popularity among cricket enthusiasts worldwide. IPL 2016 showcased the competitive spirit, talent, and entertainment value that the league consistently delivers, making it a highly anticipated event year after year.')
    
    st.markdown('---')           


with tab9:
    st.title('IPL-2015')
    st.image('https://www.mumbaiindians.com/static-assets/waf-images/bd/b8/c1/16-9/1920-1080/article-267-may-24-1.png',width=600)
    st.caption('Champions-Mumbai Indians')
    st.write('Orange Cap winner- David Warner')
    st.write('Purple Cap winner-Dwayne Bravo')
    st.write('Man of the tournament-Andre Rusell')
    st.write('Fair Play Award-Chennai Super Kings')
    st.write('Emerging Player-Shreyas Iyer')
    st.caption('IPL 2015, the eighth edition of the Indian Premier League, was a riveting tournament that captivated cricket fans with its thrilling matches and memorable moments. Spanning from April 8 to May 24, 2015, the season featured eight teams competing in a double round-robin format followed by playoffs. The Mumbai Indians emerged as champions for the second time in IPL history, defeating the Chennai Super Kings in a high-stakes final. The final, held at the Eden Gardens in Kolkata, witnessed a nail-biting encounter between the two powerhouses of the tournament. Throughout the season, there were exceptional individual performances, with David Warner of the Sunrisers Hyderabad leading the run charts and Dwayne Bravo of the Chennai Super Kings claiming the Purple Cthe highest wicket-taker. IPL 2015 witnessed remarkable displays of skill and strategy, such as AB de Villiers breathtaking knock of 133 not out off just 59 balls for the Royal Challengers Bangalore, and Andre Russells all-round brilliance for the Kolkata Knight Riders. The tournament also saw the rise of young talents like Shreyas Iyer, who made a significant impact for the Delhi Daredevils. IPL 2015 also faced a major setback when two teams, the Chennai Super Kings and the Rajasthan Royals, were suspended for two seasons due to their involvement in a betting scandal. However, the overall spirit of the tournament remained intact, with packed stadiums, enthusiastic crowds, and enthralling matches that solidified the reputation as one of the premier T20 leagues in the world.')
    st.caption('In addition to the on-field action, IPL 2015 had its fair share of off-field incidents and memorable moments. One such moment was the return of Chennai Super Kings (CSK) and Rajasthan Royals (RR) after their two-year suspension. Both teams were welcomed back by their loyal fans and continued to be strong contenders throughout the season. Another significant incident was the emergence of young Indian talents like Shreyas Iyer, Sarfaraz Khan, and Deepak Hooda, who made their mark with impressive performances and showcased their potential for the national team. IPL 2015 also witnessed the retirement of cricketing legends like Michael Hussey and Jacques Kallis, who bid farewell to the sport after illustrious careers. The tournament further solidified the reputation of players like Virat Kohli, AB de Villiers, and Chris Gayle as destructive batsmen capable of demolishing any bowling attack. Off the field, IPL 2015 remained a spectacle of glitz and glamour, with cheerleaders, musical performances, and celebrity appearances enhancing the entertainment factor. The league continued to attract massive crowds and garnered high viewership ratings, further establishing itself as a premier cricketing event. Overall, IPL 2015 provided fans with moments of pure cricketing brilliance, emotional farewells, and intense rivalries, making it a memorable edition of the tournament.')
    
    st.markdown('---')      

with tab10:
    st.title('IPL-2014')
    st.image('https://drop.ndtv.com/albums/SPORTS/kkrwinningmoments/1.jpg',width=600)
    st.caption('Champions-Kolkata Knight Riders')
    st.write('Orange Cap winner- Robin Utthappa')
    st.write('Purple Cap winner-Mohit Sharma')
    st.write('Man of the tournament-Glenn Maxwell')
    st.write('Fair Play Award-Chennai Super Kings')
    st.write('Emerging Player-Axar Patel')
    st.caption('IPL 2014, the seventh edition of the Indian Premier League, was a rollercoaster ride of cricketing action filled with intense matches and notable moments. Spanning from April 16 to June 1, 2014, the season featured eight teams competing in a double round-robin format followed by playoffs. The Kolkata Knight Riders emerged as champions for the second time in IPL history, defeating the Kings XI Punjab in a thrilling final. The final, held at the M. Chinnaswamy Stadium in Bangalore, witnessed a spectacular chase by the Knight Riders, led by Manish Pandeys match-winning knock. Throughout the tournament, there were outstanding individual performances, with Robin Uthappa of the Kolkata Knight Riders leading the run charts and Mohit Sharma of the Chennai Super Kings claiming the Purple Cap as the highest wicket-taker. IPL 2014 also saw some remarkable displays of power-hitting, with Glenn Maxwell of the Kings XI Punjab setting a new record for the most sixes in a single IPL season. The tournament was not without its controversies, as it was marred by spot-fixing allegations, resulting in the suspension of Chennai Super Kings and Rajasthan Royals for two seasons. Despite the challenges, IPL 2014 showcased the resilience and competitive spirit of the players, with nail-biting matches, fierce rivalries, and incredible displays of skill. The league continued to draw massive crowds, avid viewership, and remained a global phenomenon, solidifying its position as one of the most popular T20 leagues in the world.')
    st.caption('In addition to the thrilling matches, IPL 2014 had its fair share of notable incidents and milestones. One significant moment was the exceptional batting performance by Kings XI Punjabs Glenn Maxwell, who made a tremendous impact with his aggressive strokeplay and innovative shot-making. Maxwells explosive batting earned him the nickname "The Big Show" as he set the tournament on fire with his incredible hitting. Another standout moment was the consistent form of Robin Uthappa from the Kolkata Knight Riders, who had a remarkable run with the bat and finished as the leading run-scorer of the season. The tournament also witnessed the emergence of young talents like Axar Patel, who impressed with his all-round skills for the Kings XI Punjab, and Sandeep Sharma, who displayed his bowling prowess for the same team. IPL 2014 marked the debut of two new franchises, the Sunrisers Hyderabad and the Royal Challengers Bangalore, who added a fresh dimension to the competition. The season also witnessed some outstanding captaincy, with Gautam Gambhir leading the Kolkata Knight Riders to their second title and displaying astute tactical decisions throughout the tournament. Despite the challenges posed by spot-fixing controversies, IPL 2014 showcased the resilience and excitement of the tournament, captivating cricket fans worldwide with its blend of high-quality cricket and intense rivalries.')
    
    st.markdown('---')  

with tab11:
    st.title('IPL-2013')
    st.image('https://2.bp.blogspot.com/-PnNu-LfLAVw/UaLnyCwwYHI/AAAAAAAAPsE/cXBJLUC5I7s/s1600/Mumbai-Indians-Champions-Pepsi-IPL-2013.jpg',width=600)
    st.caption('Champions-Mumbai Indians')
    st.write('Orange Cap winner- Michael Hussey')
    st.write('Purple Cap winner-Dwayne Bravo ')
    st.write('Man of the tournament-Shane Watson ')
    st.write('Fair Play Award-Chennai Super Kings')
    st.write('Emerging Player-Sanju Samson ')
    st.caption('IPL 2013, the sixth edition of the Indian Premier League, was an enthralling season showcasing exciting cricket action and unforgettable moments. Taking place from April 3 to May 26, 2013, the season featured nine teams following the addition of the Sunrisers Hyderabad franchise. The Mumbai Indians emerged as champions for the first time in IPL history, defeating the Chennai Super Kings in a thrilling final at the Eden Gardens in Kolkata. The final witnessed a tense last-ball finish with Kieron Pollard scoring the winning runs for Mumbai Indians. Throughout the tournament, standout performances included Michael Hussey of the Chennai Super Kings leading the run charts and Dwayne Bravo, also from the Chennai Super Kings, claiming the Purple Cap as the highest wicket-taker. IPL 2013 also saw impressive batting displays like Chris Gayles record-breaking century for the Royal Challengers Bangalore. Young talents such as Sanju Samson and Shikhar Dhawan made significant contributions to their respective teams. Despite spot-fixing scandals leading to the suspension of players and investigations, IPL 2013 entertained fans with its high-scoring matches and packed stadiums, reinforcing its status as a premier T20 competition.')
    st.caption('In addition to the thrilling matches, IPL 2013 had its fair share of memorable moments and milestones. Chris Gayles record-breaking century against the Pune Warriors India, where he reached the landmark in just 30 balls, was an astonishing feat that showcased his destructive batting prowess. The season also witnessed the emergence of young talents like Sanju Samson, who became the youngest player to score a half-century in IPL history, and Shikhar Dhawan, who captained the Sunrisers Hyderabad with great success. The tournament also featured some remarkable bowling performances, with James Faulkners incredible hat-trick for the Rajasthan Royals being one of the highlights. IPL 2013 was not without controversy, as the spot-fixing scandal involving certain players and team officials tarnished the image of the league. However, the Board of Control for Cricket in India (BCCI) took strict action against those involved, reinforcing the leagues commitment to maintaining integrity. Despite the challenges, IPL 2013 remained a spectacle of high-quality cricket, packed stadiums, and enthusiastic crowds. It continued to captivate fans with its mix of established stars, emerging talents, and the thrill of close encounters. The season further solidified the IPL"s position as one of the most popular and competitive T20 leagues in the world.')
    
    st.markdown('---')           

with tab12:
    st.title('IPL-2012')
    st.image('https://www.hindustantimes.com/ht-img/img/2023/05/03/1600x900/kkr-2012_1683127970206_1683127976571.jpg',width=600)
    st.caption('Champions-Kolkata Knight Riders')
    st.write('Orange Cap winner- Chris Gayle')
    st.write('Purple Cap winner-Morne Morkel ')
    st.write('Man of the tournament-Sunil Narine ')
    st.write('Fair Play Award-Rajasthan Royals')
    st.write('Emerging Player-Mandeep Singh ')
    st.caption('IPL 2012, the fifth edition of the Indian Premier League, was a captivating season filled with thrilling cricketing action and memorable moments. Spanning from April 4 to May 27, 2012, the season featured nine teams competing in a round-robin format followed by playoffs. The Kolkata Knight Riders emerged as champions for the first time in IPL history, defeating the Chennai Super Kings in a closely contested final held at the MA Chidambaram Stadium in Chennai. The final showcased an excellent display of batting by Manvinder Bisla, who played a match-winning innings for the Knight Riders. Throughout the tournament, there were exceptional individual performances, with Chris Gayle of the Royal Challengers Bangalore leading the run charts and Morne Morkel of the Delhi Daredevils claiming the Purple Cap as the highest wicket-taker. IPL 2012 also witnessed some outstanding fielding displays, with Sunil Narine of the Kolkata Knight Riders being recognized for his exceptional fielding skills and winning the Best Fielder award. Despite some rain-affected matches and scheduling challenges, IPL 2012 managed to entertain fans with its competitive matches, enthusiastic crowds, and the growing popularity of the league. The tournament continued to showcase the immense talent and skill of players from around the world, solidifying the IPLs position as one of the premier T20 leagues globally.')
    st.caption('In addition to the thrilling matches and standout performances, IPL 2012 had its fair share of intriguing moments and noteworthy milestones. The season witnessed the emergence of young talents such as Mandeep Singh, who impressed with his consistent batting displays for the Kings XI Punjab, and Ajinkya Rahane, who showcased his class and skill for the Rajasthan Royals. The Deccan Chargers Dale Steyn proved to be a potent force with his exceptional fast bowling, terrorizing batsmen with his pace and accuracy. The tournament also saw some exceptional captaincy, with Gautam Gambhir leading the Kolkata Knight Riders with aplomb, making shrewd decisions and instilling a winning mentality in the team. IPL 2012 further solidified the importance of all-rounders, as players like Shane Watson, Kieron Pollard, and Dwayne Bravo made significant contributions with both bat and ball for their respective teams. The season was not without its controversies, as spot-fixing allegations marred the reputation of the league. However, the IPL took stringent actions to address these issues and maintain the integrity of the tournament. Overall, IPL 2012 was a thrilling chapter in the leagues history, captivating fans with its mix of high-quality cricket, exciting matches, and the rise of new stars.')
    
    st.markdown('---')           
         

with tab13:
    st.title('IPL-2011')
    st.image('https://www.hindustantimes.com/ht-img/img/2023/05/03/1600x900/csk-2011_1683125075626_1683125088919.jpg',width=600)
    st.caption('Champions-Chennai Super Kings')
    st.write('Orange Cap winner- Chris Gayle')
    st.write('Purple Cap winner-Lasith Malinga ')
    st.write('Man of the tournament-Chris Gayle ')
    st.write('Fair Play Award-Chennai Super Kings')
    st.write('Emerging Player-Iqbal Abdulla')
    st.caption('IPL 2011, the fourth edition of the Indian Premier League, was an action-packed season filled with exciting cricket and memorable moments. Taking place from April 8 to May 28, 2011, the tournament featured ten teams vying for the prestigious title. The Chennai Super Kings emerged as champions for the second consecutive year, defeating the Royal Challengers Bangalore in a thrilling final held at the M. A. Chidambaram Stadium in Chennai. The final saw a magnificent century by Murali Vijay, who played a crucial role in securing victory for the Super Kings. Throughout the tournament, there were outstanding individual performances, with Chris Gayle of the Royal Challengers Bangalore leading the run charts and Lasith Malinga of the Mumbai Indians claiming the Purple Cap as the highest wicket-taker. IPL 2011 also witnessed some exceptional fielding displays, with Kieron Pollard of the Mumbai Indians being recognized for his incredible athleticism and winning the Best Fielder award. Despite logistical challenges and the absence of some key international players due to national commitments, IPL 2011 continued to entertain fans with its high-intensity matches, fierce rivalries, and the emergence of young talents like Paul Valthaty, who scored a scintillating century for the Kings XI Punjab. The season further solidified the leagues popularity and demonstrated its ability to captivate cricket enthusiasts worldwide.')
    st.caption('In addition to the thrilling matches and standout performances, IPL 2011 witnessed several memorable moments and significant milestones. The tournament showcased the power-hitting prowess of Chris Gayle, who smashed a record-breaking 175 not out off just 66 balls for the Royal Challengers Bangalore against the Pune Warriors India. Gayles blistering knock included 13 fours and 17 sixes, leaving the cricketing world in awe. Another notable achievement came from Sachin Tendulkar, who became the first player to score 4,000 runs in IPL history during his innings for the Mumbai Indians. The season also featured some gripping encounters, including close finishes and high-scoring matches that kept fans on the edge of their seats. Despite a few controversies surrounding player discipline and a change in venue due to security concerns, IPL 2011 managed to entertain millions of fans and attract a massive global viewership. The success of the tournament demonstrated the growing popularity of T20 cricket and the Indian Premier League as a premier sporting event.')
    
    st.markdown('---')  
    


with tab14:
    st.title('IPL-2010')
    st.image('https://ss-i.thgim.com/public/incoming/article38471721.ece/alternates/FREE_1200/ipljfif',width=600)
    st.caption('Champions-Chennai Super Kings')
    st.write('Orange Cap winner- Sachin Tendulkar')
    st.write('Purple Cap winner-Pragyan Ojha')
    st.write('Man of the tournament-Sachin Tendulkar ')
    st.write('Fair Play Award-Chennai Super Kings')
    st.write('Emerging Player-Saurabh Tiwari')
    st.caption('IPL 2010, the third edition of the Indian Premier League, was an electrifying season filled with intense cricketing action and memorable moments. Held from March 12 to April 25, 2010, the tournament featured eight teams competing in a round-robin format followed by playoffs. The Chennai Super Kings emerged as champions, defeating the Mumbai Indians in a thrilling final held at the DY Patil Stadium in Mumbai. The final showcased a magnificent century by Suresh Raina, who played a pivotal role in Chennais victory. Throughout the tournament, there were standout performances, with Sachin Tendulkar of the Mumbai Indians leading the run charts and Pragyan Ojha of the Deccan Chargers claiming the Purple Cap as the highest wicket-taker. IPL 2010 witnessed several close matches, including nail-biting finishes and remarkable comebacks. The tournament showcased the emergence of young talents like Kieron Pollard and Manish Pandey, who made a mark with their power-hitting abilities. Despite challenges such as security concerns and logistical issues, IPL 2010 continued to captivate audiences with its high-quality cricket, fierce rivalries, and packed stadiums. The season further solidified the leagues position as one of the most popular T20 competitions worldwide, garnering massive viewership and enthusiastic support from cricket fans.')
    st.caption('In addition to the thrilling matches and standout performances, IPL 2010 had its fair share of captivating moments and notable milestones. The tournament witnessed the Brendon McCullum scoring the first century of the season, showcasing his aggressive batting style. Chris Gayle also made a significant impact with his explosive batting, scoring a quickfire century in just 30 balls against the Pune Warriors India. The season also featured impressive bowling displays, with bowlers like Praveen Kumar, Lasith Malinga, and Shane Warne showcasing their skills and contributing crucial wickets for their respective teams. IPL 2010 further highlighted the importance of team strategies and effective captaincy, with Mahendra Singh Dhoni leading the Chennai Super Kings to victory with his astute decision-making and calm demeanor. The leagues popularity continued to soar, attracting a wide range of international players and expanding its fan base. Despite occasional controversies and organizational challenges, IPL 2010 solidified the reputation as a top-notch cricketing spectacle, combining fierce competition, entertainment, and the glamour of the T20 format.')
    
    st.markdown('---')  


with tab15:
    st.title('IPL-2009')
    st.image('https://i.ytimg.com/vi/PeosKL1yLOI/maxresdefault.jpg',width=600)
    st.caption('Champions-Deccan Charges')
    st.write('Orange Cap winner- Matthew Hayden')
    st.write('Purple Cap winner-RP Singh')
    st.write('Man of the tournament-Adam Gilchrist')
    st.write('Fair Play Award-Kings XI Punjab')
    st.write('Emerging Player-Rohit Sharma')
    st.caption('IPL 2009, the second edition of the Indian Premier League, was a thrilling season filled with excitement and drama. The tournament, held from April 18 to May 24, 2009, witnessed several iconic moments and showcased the resilience of the league. Due to security concerns, IPL 2009 was moved to South Africa, bringing the IPL spectacle to a new audience. The Deccan Chargers emerged as the champions, defeating the Royal Challengers Bangalore in a closely contested final held at the Wanderers Stadium in Johannesburg. The final saw Anil Kumble, captain of the Royal Challengers Bangalore, take a remarkable five-wicket haul, but it was not enough to secure victory. Adam Gilchrist, the captain of the Deccan Chargers, played a crucial role with his explosive batting throughout the tournament. Notable performances came from players like Matthew Hayden, who displayed his power-hitting for the Chennai Super Kings, and AB de Villiers, who showcased his versatility and innovation for the Delhi Daredevils. The season also witnessed the emergence of young talents such as Manish Pandey, who became the first Indian player to score a century in the IPL. Despite logistical challenges and the absence of some international players due to national commitments, IPL 2009 managed to entertain fans with its high-quality cricket and passionate performances. The tournament showcased the global appeal of T20 cricket and established the IPL as a premier cricketing event.')
    st.caption('In addition to the thrilling matches and standout performances, IPL 2009 witnessed several memorable moments and noteworthy milestones. The tournament saw a nail-biting semifinal between the Royal Challengers Bangalore and the Chennai Super Kings, which went into a Super Over to determine the winner. The Royal Challengers Bangalore emerged victorious, securing their place in the final. The season also featured impressive bowling performances, with R.P. Singh of the Deccan Chargers taking the most wickets and earning the Purple Cap. The explosive batting of Adam Gilchrist, who led the Deccan Chargers to victory in the final, left a lasting impact on the tournament. IPL 2009 showcased the diversity and talent of international players, with teams comprising a mix of players from various cricket-playing nations. The success of the tournament in South Africa demonstrated the global appeal of the IPL and its ability to captivate audiences worldwide. Despite challenges and uncertainties, IPL 2009 proved to be a thrilling edition of the league, paving the way for future seasons to continue entertaining cricket fans around the world.')
    
    st.markdown('---')   

with tab16:
    st.title('IPL-2008')
    st.image('https://bsmedia.business-standard.com/_media/bs/img/article/2020-09/19/full/1600517014-1739.jpg?im=FeatureCrop,width=924,height=520',width=600)
    st.caption('Champions-Rajasthan Royals')
    st.write('Orange Cap-Shaun Marsh')
    #st.image('https://thefangarage.com/upload/posts/4937/0/Shaun-Marsh.jpg',width=250)
    st.write('Purple Cap-Sohail Tanvir')
    #st.image('https://static.toiimg.com/photo/68174094.cms',width=450)
    st.write('Man of the tournament-Shane Watson')
    #st.image('https://content.api.news/v3/images/bin/d22a03382c3b024ade651c453ccf342c',width=450)
    st.write('Fair Play Award-Chennai Super Kings')
    #st.image('https://e0.pxfuel.com/wallpapers/948/840/desktop-wallpaper-chennai-super-king-poster-csk-poster-ipl-team-logo.jpg',width=450)
    st.write('Emerging Player-Shreevats Goswami')
    st.caption('The 2008 Indian Premier League (IPL) was the inaugural season of the tournament, which brought together some of the best cricketers from around the world.')
    st.caption('The 2008 Indian Premier League (IPL) was a watershed moment in cricket history, introducing a franchise-based T20 tournament that captivated fans worldwide. It was initiated by the Board of Control for Cricket in India (BCCI) as a revolutionary concept to bring together international and domestic players in a high-octane format. The tournament featured eight teams: Chennai Super Kings, Delhi Daredevils (now Delhi Capitals), Kings XI Punjab (now Punjab Kings), Kolkata Knight Riders, Mumbai Indians, Rajasthan Royals, Royal Challengers Bangalore, and Deccan Chargers (now defunct). The season kicked off with Brendon McCullums electrifying 158 not out for the Kolkata Knight Riders, setting the stage for an exhilarating competition. Throughout the tournament, there were standout performances, including Shaun Marshs prolific batting, Sohail Tanvirs sensational bowling, and Shane Warnes inspiring leadership for the Rajasthan Royals. The Royals, considered underdogs, defied the odds and lifted the trophy with their cohesive team spirit. The tournament showcased the emergence of young talents like Shreevats Goswami and Ravindra Jadeja, while legendary players such as Sachin Tendulkar and Rahul Dravid displayed their prowess. The 2008 IPL left an indelible mark on the cricketing landscape, creating a new dimension of entertainment, inspiring subsequent seasons, and solidifying the leagues position')
    
