using Microsoft.AspNetCore.Mvc;
using ProjectC.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ProjectC.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class WarehousesController : ControllerBase
    {
        private readonly IWarehouseService _warehouseService;

        public WarehousesController(IWarehouseService warehouseService)
        {
            _warehouseService = warehouseService;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Warehouse>>> GetWarehouses()
        {
            var warehouses = await _warehouseService.GetWarehouses();
            if (warehouses == null)
            {
                return NotFound();
            }
            return Ok(warehouses);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Warehouse>> GetWarehouse(int id)
        {
            var warehouse = await _warehouseService.GetWarehouse(id);
            if (warehouse == null)
            {
                return NotFound();
            }
            return Ok(warehouse);
        }

        [HttpPost]
        public async Task<ActionResult<Warehouse>> AddWarehouse(Warehouse warehouse)
        {
            var createdWarehouse = await _warehouseService.AddWarehouse(warehouse);
            if (createdWarehouse == null)
            {
                return BadRequest();
            }
            return CreatedAtAction(nameof(GetWarehouse), new { id = createdWarehouse.Id }, createdWarehouse);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateWarehouse(int id, Warehouse warehouse)
        {
            if (id != warehouse.Id)
            {
                return BadRequest();
            }

            await _warehouseService.UpdateWarehouse(id, warehouse);
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteWarehouse(int id)
        {
            await _warehouseService.DeleteWarehouse(id);
            return NoContent();
        }
    }
}