using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using ProjectC.Models;

public class LocationsService : ILocationsService
{
    private readonly DataContext _context;

    public LocationsService(DataContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<Location>> GetAllAsync()
    {
        return await _context.Locations.ToListAsync();
    }

    public async Task<Location> GetByIdAsync(int id)
    {
        return await _context.Locations.FindAsync(id);
    }

    public async Task AddAsync(Location location)
    {
        location.CreatedAt = DateTime.UtcNow;
        location.UpdatedAt = DateTime.UtcNow;
        await _context.Locations.AddAsync(location);
        await _context.SaveChangesAsync();
    }

    public async Task UpdateAsync(int id, Location updatedLocation)
    {
        var location = await GetByIdAsync(id);
        if (location != null)
        {
            location.Code = updatedLocation.Code;
            location.Name = updatedLocation.Name;
            location.WarehouseId = updatedLocation.WarehouseId;
            location.UpdatedAt = DateTime.UtcNow;
            _context.Locations.Update(location);
            await _context.SaveChangesAsync();
        }
    }

    public async Task RemoveAsync(int id)
    {
        var location = await GetByIdAsync(id);
        if (location != null)
        {
            _context.Locations.Remove(location);
            await _context.SaveChangesAsync();
        }
    }
}

public interface ILocationsService
{
    Task<IEnumerable<Location>> GetAllAsync();
    Task<Location> GetByIdAsync(int id);
    Task AddAsync(Location location);
    Task UpdateAsync(int id, Location updatedLocation);
    Task RemoveAsync(int id);
}