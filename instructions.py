#JWT is used for security 

# first you have to dowload the JWT library into requirements :

#pip install flask-jwt-extended
#update requirements: pip freeze > requirements.txt

# Configure JWT with a secret key for token creation and validation.
# Choose a few routes that require authentication and protect them using Flask-JWT-Extended decorators.
# For example, use @jwt_required() to ensure that only users with valid JWT tokens can access these routes.
# Modify the logic of the protected routes to extract user information from the JWT payload.
# Utilize the user identity obtained from the JWT token for authorization and other necessary actions within the protected routes.
# Test the protected routes with valid and invalid JWT tokens to ensure proper authentication and authorization.
# Handle cases where users don't have valid tokens or are trying to access protected routes without authentication.



# Explanation of what JWT is : JWT verifies that a user has login credentials.
#When that is verified JWT spits out a token that identifies the user
# it also asigns the user a secret key
# Then you assign that token the secret key