# configuration
app.config.extend({
    'COGNITO_REGION': 'us-east-1',
    'COGNITO_USERPOOL_ID': 'us-east-1_dyJjLI57z',
    
# initialize extension
from flask_cognito import CognitoAuth
cogauth = CognitoAuth(app)

@cogauth.identity_handler
def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    return User.query.filter(User.cognito_username == payload['username']).one_or_none()