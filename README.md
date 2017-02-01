# sklearn-deployment-flask

build_model.py builds a simple random forest classifier using sklearn and dumps it to file named iris_rfc_pkl.
flask_api.py loads the sklearn model from file and starts a web service at port 9000.
post.py is used to post json data containing iris data and get the prediction.
