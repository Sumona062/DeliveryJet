def uniqueCategory(product_list):
    cat=[]
    for product in product_list:
        if product.category not in cat:
            cat.append(product.category)


    return cat


def uniqueCompanyType(companies):
    cat=[]
    for com in companies:
        if com.companymodel.type not in cat:
            cat.append(com.companymodel.type)


    return cat


