## Flask Application Design
### HTML Files

- `index.html`: This will be the landing page of the website and will provide a brief overview of the application and its purpose. It will also include links to the various sections of the website, such as the recipes for North Indian and South Indian dishes, as well as a search bar for finding specific recipes.
- `north_indian_recipes.html`: This HTML file will contain the recipes for various popular North Indian dishes. The recipes will be organized into categories, such as appetizers, main courses, desserts, etc. Each recipe will include a title, a brief description, a list of ingredients, and step-by-step instructions on how to prepare the dish.
- `south_indian_recipes.html`: This HTML file will follow a similar structure to `north_indian_recipes.html`, but it will contain recipes for popular South Indian dishes.
- `recipe_detail.html`: This HTML file will be used to display the details of a specific recipe. It will include the recipe title, a brief description, a list of ingredients, and step-by-step instructions on how to prepare the dish. It will also include an image of the finished dish.
- `search.html`: This HTML file will contain a search bar and a list of search results. When a user enters a search query, the application will filter the recipes based on the query and display the results in this file.

### Routes

- `/`: This route will handle the requests for the landing page, which is `index.html`.
- `/north_indian_recipes`: This route will handle the requests for the page containing the recipes for North Indian dishes, which is `north_indian_recipes.html`.
- `/south_indian_recipes`: This route will handle the requests for the page containing the recipes for South Indian dishes.
- `/recipe_detail/<recipe_id>`: This route will handle the requests for the page displaying the details of a specific recipe, which is `recipe_detail.html`.
- `/search`: This route will handle the requests for the search page. The request will contain a `query` parameter, which is the search query entered by the user. The route will then filter the recipes based on the query and display the results in `search.html`.