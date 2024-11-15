using Microsoft.EntityFrameworkCore;
using ProjectC.Models;

public class DataContext : DbContext
{
    public DataContext(DbContextOptions<DataContext> options) : base(options)
    {
    }

    public DbSet<Client> Clients { get; set; }
    public DbSet<Order> Orders { get; set; }
    public DbSet<Shipment> Shipments { get; set; }
    public DbSet<Item> Items { get; set; }
    public DbSet<Supplier> Suppliers { get; set; }
    public DbSet<Inventory> Inventories { get; set; }
    public DbSet<ItemGroup> ItemGroups { get; set; }
    public DbSet<ItemLine> ItemLines { get; set; }
    public DbSet<ItemType> ItemTypes { get; set; }
    public DbSet<Location> Locations { get; set; }
    public DbSet<Warehouse> Warehouses { get; set; }
    public DbSet<Transfer> Transfers { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Client>().ToTable("Clients");
        modelBuilder.Entity<Order>().ToTable("Orders");
        modelBuilder.Entity<Shipment>().ToTable("Shipments");
        modelBuilder.Entity<Item>().ToTable("Items");
        modelBuilder.Entity<Supplier>().ToTable("Suppliers");
        modelBuilder.Entity<Inventory>().ToTable("Inventories");
        modelBuilder.Entity<ItemGroup>().ToTable("ItemGroups");
        modelBuilder.Entity<ItemLine>().ToTable("ItemLines");
        modelBuilder.Entity<ItemType>().ToTable("ItemTypes");
        modelBuilder.Entity<Location>().ToTable("Locations");
        modelBuilder.Entity<Warehouse>().ToTable("Warehouses");
        modelBuilder.Entity<Transfer>().ToTable("Transfers");

        modelBuilder.Entity<Order>()
            .HasMany(o => o.Items);

        modelBuilder.Entity<Shipment>()
            .HasMany(s => s.Items);
    }
}
