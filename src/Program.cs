using Microsoft.EntityFrameworkCore;

public class Program
{
    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen();

        builder.Services.AddControllers();

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

        builder.Services.AddCors(options =>
        {
            options.AddPolicy("AllowAllOrigins", builder =>
            {
                builder.AllowAnyOrigin()
                       .AllowAnyMethod()
                       .AllowAnyHeader();
            });
        });
        builder.Services.AddScoped<ILocationService, LocationsService>();
        builder.Services.AddScoped<IWarehouseService, WarehouseService>();
        builder.Services.AddScoped<ITransferService, TransferService>();

        var app = builder.Build();

        if (app.Environment.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI();
        }

        app.UseHttpsRedirection();
        app.UseCors("AllowAllOrigins");

        app.UseAuthorization();
        app.MapControllers();

        /*
            TODO: Fix api key validation
        */
        app.Use((context, next) =>
        {
            if(context.Request.Headers.ContainsKey("API_KEY")){
                var key = context.Request.Headers["API_KEY"];
                if(key == "a1b2c3b4"){
                    return next();
                }
            }
            context.Response.StatusCode = 401;
            return Task.CompletedTask;
                        
        });

        app.Run("http://localhost:8000");
    }

}
