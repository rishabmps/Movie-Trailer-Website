import media,fresh_tomatoes
toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that came to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story1 = media.Movie("Toy Story", 
	"A story of a boy and his toys that came to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story2 = media.Movie("Toy Story", 
	"A story of a boy and his toys that came to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")
toy_story3 = media.Movie("Toy Story", 
	"A story of a boy and his toys that came to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=JcpWXaA2qeg")
movies = [toy_story,toy_story1,toy_story2,toy_story3]
fresh_tomatoes.open_movies_page(movies)