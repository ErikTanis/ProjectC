using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v1/suppliers")]
public class SuppliersController : ControllerBase
{

    private readonly ISupplierService _supplierService;

    public SuppliersController(ISupplierService supplierService){
        _supplierService = supplierService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Supplier>), 200)]
    public async Task<IActionResult> GetSuppliers(){
        IEnumerable<Supplier>? suppliers = await _supplierService.GetSuppliers();
        return suppliers == null ? NotFound() : Ok( suppliers );
    }


    [HttpGet("{supplier_id}")]
    [ProducesResponseType(typeof(Supplier), 200)]
    public async Task<IActionResult> GetSupplier(int supplier_id){
        Supplier? supplier = await _supplierService.GetSupplier(supplier_id);
        return supplier == null ? NotFound() : Ok( supplier );
    }


    [HttpGet("{supplier_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<Item>), 200)]
    public async Task<IActionResult> GetSupplierItems(int supplier_id){
        IEnumerable<Item>? items = await _supplierService.GetItems(supplier_id);
        return items == null ? NotFound() : Ok( items );
    }


    [HttpPost("")]
    [ProducesResponseType(typeof(Supplier), 201)]
    public async Task<IActionResult> AddSupplier([FromBody] Supplier supplier){
        Supplier? supplier1 = await _supplierService.AddSupplier(supplier);
        return supplier1 == null ? StatusCode(500) : CreatedAtAction(nameof(GetSupplier), new { supplier_id = supplier1.Id }, supplier1);
    }


    [HttpPut("{supplier_id}")]
    [ProducesResponseType(typeof(Supplier), 200)]
    public async Task<IActionResult> UpdateSupplier(int supplier_id, [FromBody] Supplier supplier){
        Supplier? supplier1 = await _supplierService.UpdateSupplier(supplier_id, supplier);
        return supplier1 == null ? StatusCode(500) : Ok( supplier1 );
    }


    [HttpDelete("{supplier_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteSupplier(int supplier_id){
        await _supplierService.DeleteSupplier(supplier_id);
        return NoContent();
    }


}