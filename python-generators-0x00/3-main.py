lazy_paginate = __import__('2-lazy_paginate').lazy_paginate

print("Paginated results (lazy loaded):")
for page in lazy_paginate(3):
    print(" New Page")
    for user in page:
        print(user)