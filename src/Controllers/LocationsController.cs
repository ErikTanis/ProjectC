using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using ProjectC.Models;
using ProjectC.Services;

namespace ProjectC.Controllers
{
    [Route("api/v1/locations")]
    [ApiController]
    public class LocationsController : ControllerBase
    {
        private readonly LocationsService _locationsService;

        public LocationsController()
        {
            _locationsService = new LocationsService();
        }

        [HttpGet]
        public ActionResult<IEnumerable<Location>> GetAll()
        {
            var locations = _locationsService.GetAll();
            return Ok(locations);
        }

        [HttpGet("{id}")]
        public ActionResult<Location> GetById(int id)
        {
            var location = _locationsService.GetById(id);
            if (location == null)
            {
                return NotFound();
            }
            return Ok(location);
        }

        [HttpPost]
        public ActionResult<Location> Add([FromBody] Location location)
        {
            _locationsService.Add(location);
            return CreatedAtAction(nameof(GetById), new { id = location.Id }, location);
        }

        [HttpPut("{id}")]
        public IActionResult Update(int id, [FromBody] Location location)
        {
            var existingLocation = _locationsService.GetById(id);
            if (existingLocation == null)
            {
                return NotFound();
            }

            _locationsService.Update(id, location);
            return NoContent();
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var location = _locationsService.GetById(id);
            if (location == null)
            {
                return NotFound();
            }

            _locationsService.Remove(id);
            return NoContent();
        }
    }
}
