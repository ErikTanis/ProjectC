using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ProjectC.Models;

namespace ProjectC.Controllers
{
    [Route("api/v1/locations")]
    [ApiController]
    public class LocationsController : ControllerBase
    {
        private readonly LocationsService _locationsService;

        public LocationsController(LocationsService locationsService)
        {
            _locationsService = locationsService;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Location>>> GetAll()
        {
            var locations = await _locationsService.GetAllAsync();
            return locations == null ? NotFound() : Ok(locations);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Location>> GetById(int id)
        {
            var location = await _locationsService.GetByIdAsync(id);
            if (location == null)
            {
                return NotFound();
            }
            return Ok(location);
        }

        [HttpPost]
        public async Task<ActionResult<Location>> Add([FromBody] Location location)
        {
            await _locationsService.AddAsync(location);
            return CreatedAtAction(nameof(GetById), new { id = location.Id }, location);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> Update(int id, [FromBody] Location location)
        {
            var existingLocation = await _locationsService.GetByIdAsync(id);
            if (existingLocation == null)
            {
                return NotFound();
            }

            await _locationsService.UpdateAsync(id, location);
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            var location = await _locationsService.GetByIdAsync(id);
            if (location == null)
            {
                return NotFound();
            }

            await _locationsService.RemoveAsync(id);
            return NoContent();
        }
    }
}
