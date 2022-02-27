# API 
### **GET** `/api/items/`
Получение списка элементов.

#### Query params:
| name | type                | description                                                                   |
| ---- |---------------------|-------------------------------------------------------------------------------|
| page | int                 | Номер страницы                                                                |
| sorting | string              | Поле для сортировки                                                           |
| filter_field | string              | Поле для фильтрации                                                           |
| filter_type | string              | Способ фильтрации: `lt` - меньме, `gt` - больше, `eq` - равно, `in` - содержит |
| filter_value | string / int / date | Значение для фильтрации                                                       |

#### Sample output:
```json
{
  "total_page": 0,
  "items": [
    {
      "item_id": 0,
      "date": "1970-01-01",
      "name": "String",
      "count": 0,
      "distance": 0.0
    }
  ]
}
```