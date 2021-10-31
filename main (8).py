our_products = {"Apple", "Tesla", "McDonald's"}
range_of_the_company_1 = {"Samsung", "Sony"}
range_of_the_company_2 = {"Apple", "IBM", "Tesla"}
range_of_the_company_3 = {"BMW", "Tesla", "Ferrari"}
print(our_products.intersection(range_of_the_company_1))
print(our_products.intersection(range_of_the_company_2))
print(our_products.intersection(range_of_the_company_3))
print(our_products.difference(range_of_the_company_1))
print(our_products.difference(range_of_the_company_2))
print(our_products.difference(range_of_the_company_3))
print(our_products.symmetric_difference(range_of_the_company_1))
print(our_products.symmetric_difference(range_of_the_company_2))
print(our_products.symmetric_difference(range_of_the_company_3))
our_products.intersection_update(range_of_the_company_1)
print(our_products)
our_products.discard("IBM")
our_products.discard("Apple")