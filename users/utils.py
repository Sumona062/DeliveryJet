def uniqueCategory(product_list):
    cat=[]
    for product in product_list:
        if product.category not in cat:
            cat.append(product.category)


    return cat
