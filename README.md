# school_mart
Trading platform for students

Installation guide:
Install python
install django (pip install django)
install djangorestframework(pip install djangorestframework)
install pillow(pip install pillow)


how to use:
run python3 manage.py runserver on the terminal

API Documentation:

127.0.0.1:8000/api/users (end point for app users)
{
  post request to add new users
  delete removes users
}
127.0.0.1:8000/api/product (end point for product)
{
  get request to list products
  post request to add new products
  delete removes products
}
127.0.0.1:8000/api/store (end point for store)
{
  get request to list stores
  post request to add new stores
  delete removes stores
}
127.0.0.1:8000/api/profile (end point for profiles)
{
  get request to list profiles
  post request to add new profiles
  delete removes profiles
}
