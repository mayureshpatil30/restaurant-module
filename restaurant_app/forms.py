from app import app
from flask import render_template
from app.forms import newRestaurantForm, editRestaurantForm, deleteRestaurantForm, addMenuForm, editMenuForm, deleteMenuForm


@app.route('/')
@app.route('/restaurant', methods=['GET', 'POST'])
def Restaurant():
    # This page wil show all my restaurant.
    return render_template('restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:table_id>/edit/', methods=['GET', 'POST'])
def edittable(table_id):
    # This page will be for editing table
    form = edittableForm()
    return render_template('edittable.html', form=form)

@app.route('/restaurant/<int:table_id>/delete', methods=['GET', 'POST'])
def deletetable(table_id):
    # This page will be for deleting table
    form = deletetableForm()
    return render_template('deletetable.html', form=form)

@app.route('/restaurant/<int:table_id>/', methods=['GET', 'POST'])
@app.route('/restaurant/<int:table_id>/menu')
def showMenu(table_id):
    # This page is the menu for restaurant
    return render_template('menu.html')

@app.route('/restaurant/<int:table_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(table_id):
    # This page is for making a new menu item for restaurant
    form = addMenuForm()
    return render_template('newMenuItem.html', form=form)

@app.route('/restaurant/<int:table_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(table_id, menu_id):
    # This page is for editing menu item"
    form = editMenuForm()
    return render_template('editMenuItem.html', form=form)

@app.route('/restaurant/<int:table_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(table_id, menu_id):
    # This page is for deleting menu item %s
    form = editMenuForm()
    return render_template('deleteMenuItem.html', form=form)