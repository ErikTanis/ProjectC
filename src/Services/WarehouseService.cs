using Microsoft.EntityFrameworkCore;
using ProjectC.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

public class WarehouseService : IWarehouseService
{
    private readonly DataContext _context;

    public WarehouseService(DataContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<Warehouse>?> GetWarehouses()
    {
        return await _context.Warehouses.ToListAsync();
    }

    public async Task<Warehouse?> GetWarehouse(int warehouseId)
    {
        return await _context.Warehouses.FindAsync(warehouseId);
    }

    public async Task<Warehouse?> AddWarehouse(Warehouse warehouse)
    {
        warehouse.CreatedAt = DateTime.Now;
        warehouse.UpdatedAt = DateTime.Now;
        await _context.Warehouses.AddAsync(warehouse);
        await _context.SaveChangesAsync();
        return await GetWarehouse(warehouse.Id);
    }

    public async Task UpdateWarehouse(int warehouseId, Warehouse warehouse)
    {
        warehouse.Id = warehouseId;
        warehouse.UpdatedAt = DateTime.Now;
        _context.Warehouses.Update(warehouse);
        await _context.SaveChangesAsync();
    }

    public async Task DeleteWarehouse(int warehouseId)
    {
        Warehouse? warehouse = await _context.Warehouses.FindAsync(warehouseId);
        if (warehouse == null) return;
        _context.Warehouses.Remove(warehouse);
        await _context.SaveChangesAsync();
    }
}

public interface IWarehouseService
{
    Task<IEnumerable<Warehouse>?> GetWarehouses();
    Task<Warehouse?> GetWarehouse(int warehouseId);
    Task<Warehouse?> AddWarehouse(Warehouse warehouse);
    Task UpdateWarehouse(int warehouseId, Warehouse warehouse);
    Task DeleteWarehouse(int warehouseId);
}
