using Microsoft.EntityFrameworkCore;

public class Program
{
    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen();

        builder.Services.AddDbContext<DataContext>(options =>
        {
            options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection"));
        });

        builder.Services.AddScoped<IOrderService, OrderService>();
        builder.Services.AddScoped<IShipmentService, ShipmentService>();
        builder.Services.AddScoped<ISupplierService, SupplierService>();
        builder.Services.AddScoped<IClientService, ClientService>();
        builder.Services.AddScoped<IInventoryService, InventoryService>();
        builder.Services.AddScoped<IItemService, ItemService>();
        builder.Services.AddScoped<IItemGroupService, ItemGroupService>();
        builder.Services.AddScoped<IItemLinesService, ItemLinesService>();
        builder.Services.AddScoped<IItemTypeService, ItemTypeService>();

        var app = builder.Build();

        if (app.Environment.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI();
        }

        app.UseHttpsRedirection();


        app.Run();
    }

}

