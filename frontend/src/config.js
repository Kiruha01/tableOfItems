export default Object.freeze({
    TABLE_HEADERS: ["Дата", "Название", "Количество", "Расстояние"],
    SORTING_FIELDS: [{name: "name", title: "Название"}, {name: "count", title: "Количество"},
        {name: "distance", title: "Расстояние"}],
    FILTERING_FIELDS: [{name: "date", title: "Дата"}, {name: "name", title: "Название"},
        {name: "count", title: "Количество"}, {name: "distance", title: "Расстояние"}],
    FILTERING_TYPES: [{name: 'eq', title: 'равно'}, {name: 'lt', title: 'меньше чем'}, {name: 'gt', title: 'больше чем'},
        {name: 'in', title: 'содержит'}]
})