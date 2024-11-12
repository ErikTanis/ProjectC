using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using ProjectC.Models;

namespace ProjectC.Services
{
    public class LocationsService(DataContext context)
    {
        private readonly DataContext _context = context;

        public async Task<IEnumerable<Location>> GetAllAsync()
        {
            return await _context.Locations.ToListAsync();
        }

        public async Task<Location> GetByIdAsync(int id)
        {
            var location = await _context.Locations.FindAsync(id);
            if (location == null)
            {
                throw new KeyNotFoundException($"Location with id {id} not found.");
            }
            return location;
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
}
