using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/orders")]
public class OrdersController : ControllerBase
{

    private readonly IOrderService _orderService;

    public OrdersController(IOrderService orderService){
        _orderService = orderService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Order>), 200)]
    public async Task<IActionResult> GetAllOrders(){
        IEnumerable<Order> orders = await _orderService.GetOrders();
        return Ok( orders );
    }


    [HttpGet("{order_id}")]
    [ProducesResponseType(typeof(Order), 200)]
    public async Task<IActionResult> GetOrder(string order_id){
        Order? order = await _orderService.GetOrder(order_id);
        if(order == null){
            return NotFound();
        }
        return Ok( order );
    }


    [HttpGet("{order_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<ItemInfo>), 200)]
    public async Task<IActionResult> GetOrderItems(string order_id){
        IEnumerable<ItemInfo>? items = await _orderService.GetOrderItems(order_id);
        if(items == null){
            return NotFound();
        }
        return Ok( items );
    }


    [HttpPost("")]
    [ProducesResponseType(201)]
    public async Task<IActionResult> CreateOrder([FromBody] Order order){
        await _orderService.AddOrder(order);
        return CreatedAtAction(nameof(GetOrder), new { order_id = order.Id }, order);
    }

    [HttpPut("{order_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> EditOrder(string order_id, [FromBody] Order order){
        await _orderService.EditOrder(order_id, order);
        return NoContent();
    }


    [HttpPut("{order_id}/items")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> EditOrderItems(string order_id, [FromBody] IEnumerable<ItemInfo> items){
        //await _orderService.EditOrderItems(order_id, items);
        return NoContent();
    }


    [HttpDelete("{order_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteOrder(string order_id){
        await _orderService.DeleteOrder(order_id);
        return NoContent();
    }

}