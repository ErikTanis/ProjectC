def handle_get_version_1(self, path, user):
       if not auth_provider.has_access(user, path, "get"):
            self.send_response(403)
            self.end_headers()
            return
        # /api/v1/warehouses
        if path[0] == "warehouses":
            paths = len(path)
            match paths:
                # /api/v1/warehouses
                case 1:
                    warehouses = data_provider.fetch_warehouse_pool().get_warehouses()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouses).encode("utf-8"))
                # /api/v1/warehouses/{warehouse_id}
                case 2:
                    warehouse_id = int(path[1])
                    warehouse = data_provider.fetch_warehouse_pool().get_warehouse(warehouse_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(warehouse).encode("utf-8"))
                # /api/v1/warehouses/{warehouse_id}/locations
                case 3:
                    if path[2] == "locations":
                        warehouse_id = int(path[1])
                        locations = data_provider.fetch_location_pool(
                        ).get_locations_in_warehouse(warehouse_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(locations).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        # /api/v1/locations
        elif path[0] == "locations":
            paths = len(path)
            match paths:
                # /api/v1/locations
                case 1:
                    locations = data_provider.fetch_location_pool().get_locations()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(locations).encode("utf-8"))
                # /api/v1/locations/{location_id}
                case 2:
                    location_id = int(path[1])
                    location = data_provider.fetch_location_pool().get_location(location_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(location).encode("utf-8"))
                case _:
                    self.send_response(404)
                    self.end_headers()
        # /api/v1/transfers
        elif path[0] == "transfers":
            paths = len(path)
            match paths:
                # /api/v1/transfers
                case 1:
                    transfers = data_provider.fetch_transfer_pool().get_transfers()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfers).encode("utf-8"))
                # /api/v1/transfers/{transfer_id}
                case 2:
                    transfer_id = int(path[1])
                    transfer = data_provider.fetch_transfer_pool().get_transfer(transfer_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transfer).encode("utf-8"))
                # /api/v1/transfers/{transfer_id}/items
                case 3:
                    if path[2] == "items":
                        transfer_id = int(path[1])
                        items = data_provider.fetch_transfer_pool().get_items_in_transfer(transfer_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        # /api/v1/items
        elif path[0] == "items":
            paths = len(path)
            match paths:
                # /api/v1/items
                case 1:
                    items = data_provider.fetch_item_pool().get_items()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(items).encode("utf-8"))
                # /api/v1/items/{item_id}
                case 2:
                    item_id = int(path[1])
                    item = data_provider.fetch_item_pool().get_item(item_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item).encode("utf-8"))
                # /api/v1/items/{item_id}/inventory
                case 3:
                    if path[2] == "inventory":
                        item_id = int(path[1])
                        inventories = data_provider.fetch_inventory_pool().get_inventories_for_item(item_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(
                                inventories).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                # /api/v1/items/{item_id}/inventory/totals
                case 4:
                    if path[2] == "inventory" and path[3] == "totals":
                        item_id = int(path[1])
                        totals = data_provider.fetch_inventory_pool().get_inventory_totals_for_item(item_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(totals).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        # /api/v1/item_lines
        elif path[0] == "item_lines":
            paths = len(path)
            match paths:
                case 1:
                    item_lines = data_provider.fetch_item_line_pool().get_item_lines()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_lines).encode("utf-8"))
                case 2:
                    item_line_id = int(path[1])
                    item_line = data_provider.fetch_item_line_pool().get_item_line(item_line_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_line).encode("utf-8"))
                case 3:
                    if path[2] == "items":
                        item_line_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_line(item_line_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))                        git pull origin main - -allow-unrelated-histories
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "item_groups":
            paths = len(path)
            match paths:
                case 1:
                    item_groups = data_provider.fetch_item_group_pool().get_item_groups()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_groups).encode("utf-8"))
                case 2:
                    item_group_id = int(path[1])
                    item_group = data_provider.fetch_item_group_pool().get_item_group(item_group_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_group).encode("utf-8"))
                case 3:
                    if path[2] == "items":
                        item_group_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_group(item_group_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "item_types":
            paths = len(path)
            match paths:
                case 1:
                    item_types = data_provider.fetch_item_type_pool().get_item_types()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_types).encode("utf-8"))
                case 2:
                    item_type_id = int(path[1])
                    item_type = data_provider.fetch_item_type_pool().get_item_type(item_type_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(item_type).encode("utf-8"))
                case 3:
                    if path[2] == "items":
                        item_type_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_item_type(item_type_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "inventories":
            paths = len(path)
            match paths:
                case 1:
                    inventories = data_provider.fetch_inventory_pool().get_inventories()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventories).encode("utf-8"))
                case 2:
                    inventory_id = int(path[1])
                    inventory = data_provider.fetch_inventory_pool().get_inventory(inventory_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(inventory).encode("utf-8"))
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "suppliers":
            paths = len(path)
            match paths:
                case 1:
                    suppliers = data_provider.fetch_supplier_pool().get_suppliers()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(suppliers).encode("utf-8"))
                case 2:
                    supplier_id = int(path[1])
                    supplier = data_provider.fetch_supplier_pool().get_supplier(supplier_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(supplier).encode("utf-8"))
                case 3:
                    if path[2] == "items":
                        supplier_id = int(path[1])
                        items = data_provider.fetch_item_pool().get_items_for_supplier(supplier_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 1:
                    orders = data_provider.fetch_order_pool().get_orders()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(orders).encode("utf-8"))
                case 2:
                    order_id = int(path[1])
                    order = data_provider.fetch_order_pool().get_order(order_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(order).encode("utf-8"))
                case 3:
                    if path[2] == "items":
                        order_id = int(path[1])
                        items = data_provider.fetch_order_pool().get_items_in_order(order_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "clients":
            paths = len(path)
            match paths:
                case 1:
                    clients = data_provider.fetch_client_pool().get_clients()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(clients).encode("utf-8"))
                case 2:
                    client_id = int(path[1])
                    client = data_provider.fetch_client_pool().get_client(client_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(client).encode("utf-8"))
                case 3:
                    if path[2] == "orders":
                        client_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_for_client(client_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 1:
                    shipments = data_provider.fetch_shipment_pool().get_shipments()
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipments).encode("utf-8"))
                case 2:
                    shipment_id = int(path[1])
                    shipment = data_provider.fetch_shipment_pool().get_shipment(shipment_id)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(shipment).encode("utf-8"))
                case 3:
                    if path[2] == "orders":
                        shipment_id = int(path[1])
                        orders = data_provider.fetch_order_pool().get_orders_in_shipment(shipment_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(orders).encode("utf-8"))
                    elif path[2] == "items":
                        shipment_id = int(path[1])
                        items = data_provider.fetch_shipment_pool().get_items_in_shipment(shipment_id)
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(items).encode("utf-8"))
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
