using System;
using System.Collections.Generic;
using System.Linq;
using ProjectC.Models;

namespace ProjectC.Services
{
    public class LocationsService
    {
        private readonly List<Location> _locations;

        public LocationsService()
        {
            _locations = new List<Location>();
            // Seed data can be added here if needed
        }

        public IEnumerable<Location> GetAll()
        {
            return _locations;
        }

        public Location GetById(int id)
        {
            return _locations.FirstOrDefault(location => location.Id == id)!;
        }

        public void Add(Location location)
        {
            location.CreatedAt = DateTime.UtcNow;
            location.UpdatedAt = DateTime.UtcNow;
            _locations.Add(location);
        }

        public void Update(int id, Location updatedLocation)
        {
            var location = GetById(id);
            if (location != null)
            {
                location.Code = updatedLocation.Code;
                location.Name = updatedLocation.Name;
                location.WarehouseId = updatedLocation.WarehouseId;
                location.UpdatedAt = DateTime.UtcNow;
            }
        }

        public void Remove(int id)
        {
            var location = GetById(id);
            if (location != null)
            {
                _locations.Remove(location);
            }
        }
    }
}
