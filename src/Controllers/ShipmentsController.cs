using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/shipments")]
public class ShipmentsController : ControllerBase
{

    private readonly IShipmentService _shipmentService;

    public ShipmentsController(IShipmentService shipmentService){
        _shipmentService = shipmentService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Shipment>), 200)]
    public async Task<IActionResult> GetAllShipments(){
        IEnumerable<Shipment> shipments = await _shipmentService.GetShipments();
        return Ok( shipments );
    }

    [HttpGet("{shipment_id}")]
    [ProducesResponseType(typeof(Shipment), 200)]
    public async Task<IActionResult> GetShipment(int shipment_id){
        Shipment? shipment = await _shipmentService.GetShipment(shipment_id);
        if(shipment == null){
            return NotFound();
        }
        return Ok( shipment );
    }


    [HttpGet("{shipment_id}/orders")]
    [ProducesResponseType(typeof(IEnumerable<Order>), 200)]
    public async Task<IActionResult> GetShipmentOrders(int shipment_id){
        IEnumerable<Order>? orders = await _shipmentService.GetShipmentOrders(shipment_id);
        if(orders == null){
            return NotFound();
        }
        return Ok( orders );
    }


    [HttpGet("{shipment_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<ItemInfo>), 200)]
    public async Task<IActionResult> GetShipmentItems(int shipment_id){
        IEnumerable<ItemInfo>? items = await _shipmentService.GetShipmentItems(shipment_id);
        if(items == null){
            return NotFound();
        }
        return Ok( items );
    }


    [HttpPost("")]
    [ProducesResponseType(201)]
    public async Task<IActionResult> CreateShipment([FromBody] Shipment shipment){
        await _shipmentService.AddShipment(shipment);
        return CreatedAtAction(nameof(GetShipment), new { shipment_id = shipment.Id }, shipment);
    }


    [HttpPut("{shipment_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> EditShipment(int shipment_id, [FromBody] Shipment shipment){
        await _shipmentService.EditShipment(shipment_id, shipment);
        return NoContent();
    }


    [HttpPut("{shipment_id}/orders")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> EditShipmentOrders(int shipment_id, [FromBody] IEnumerable<Order> orders){
        await _shipmentService.EditShipmentOrders(shipment_id, orders);
        return NoContent();
    }


    [HttpPut("{shipment_id}/items")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> EditShipmentItems(int shipment_id, [FromBody] IEnumerable<ItemInfo> items){
        await _shipmentService.EditShipmentItems(shipment_id, items);
        return NoContent();
    }


    [HttpPut("{shipment_id}/commit")]
    public Task<IActionResult> CommitShipment(int shipment_id){
        throw new NotImplementedException();
    }


    [HttpDelete("{shipment_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteShipment(int shipment_id){
        await _shipmentService.DeleteShipment(shipment_id);
        return NoContent();
    }

}