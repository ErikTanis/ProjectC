using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v1/clients")]
public class ClientsController : ControllerBase
{

    private readonly IClientService _clientService;

    public ClientsController(IClientService clientService){
        _clientService = clientService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Client>), 200)]
    public async Task<IActionResult> GetClients(){
        IEnumerable<Client>? clients = await _clientService.GetClients();
        return clients == null ? NotFound() : Ok( clients );
    }


    [HttpGet("{client_id}")]
    [ProducesResponseType(typeof(Client), 200)]
    public async Task<IActionResult> GetClient(int client_id){
        Client? client = await _clientService.GetClient(client_id);
        return client == null ? NotFound() : Ok( client );
    }


    [HttpGet("{client_id}/orders")]
    [ProducesResponseType(typeof(IEnumerable<Order>), 200)]
    public async Task<IActionResult> GetClientOrders(int client_id){
        IEnumerable<Order>? orders = await _clientService.GetOrders(client_id);
        return orders == null ? NotFound() : Ok( orders );
    }


    [HttpPost("")]
    [ProducesResponseType(typeof(Client), 201)]
    public async Task<IActionResult> AddClient([FromBody] Client client){
        Client? client1 = await _clientService.AddClient(client);
        return client1 == null ? StatusCode(500) : CreatedAtAction(nameof(GetClient), new { client_id = client1.Id }, client1);
    }


    [HttpPut("{client_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> UpdateClient(int client_id, [FromBody] Client client){
        await _clientService.UpdateClient(client_id, client);
        return NoContent();
    }


    [HttpDelete("{client_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteClient(int client_id){
        await _clientService.DeleteClient(client_id);
        return NoContent();
    }

}