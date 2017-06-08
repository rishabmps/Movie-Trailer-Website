import media
import fresh_tomatoes

# Instances of Movie class
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://goo.gl/CJRIfK",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
die_hard = media.Movie("Die Hard",
                       "Just as Detective McClane lands in LA to spend \
                       Christmas with his wife, he learns about a hostage \
                       situation in an office building. Hans Gruber is the \
                       culprit and McClane's wife is one of the hostages.",
                       "https://goo.gl/IuWqKZ",
                       "https://www.youtube.com/watch?v=-qxBXm7ZUTM")
inside_out = media.Movie("Inside Out",
                         "Eleven-year-old Riley has moved to San Francisco,\
                          leaving behind her life in Minnesota. She and her \
                           five core emotions, Fear, Anger, Joy, Disgust and \
                           Sadness, struggle to cope with her new life.",
                         "https://goo.gl/DlCgtM",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")
inception = media.Movie("Inception",
                        "Cobb steals information from his targets by entering\
                         their dreams. He is wanted for his alleged role in\
                          his wife's murder and his only chance at redemption \
                          is to perform the impossible, an inception.",
                        "https://goo.gl/BqqO74",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
avatar = media.Movie("Avatar",
                     "A story of a boy and his toys that came to life",
                     "https://goo.gl/xs4zqT",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
baahubali = media.Movie("Baahubali: The Beginning",
                        "In the kingdom of Mahishmati, while pursuing his love,\
                         Shivudu learns about the conflict-ridden past of his \
                         family and his legacy. He must now prepare himself to\
                          face his new-found archenemy.",
                        "https://goo.gl/51XLcQ",
                        "https://www.youtube.com/watch?v=VdafjyFK3ko")

# movies list that will be passed in open_movies_page method
movies = [toy_story, die_hard, inside_out, inception, avatar, baahubali]

# call to generate html file
fresh_tomatoes.open_movies_page(movies)
