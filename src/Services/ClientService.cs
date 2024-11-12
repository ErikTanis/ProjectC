using Microsoft.EntityFrameworkCore;

public class ClientService : IClientService
{

    private readonly DataContext _context;

    public ClientService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<Client>?> GetClients(){
        return await _context.Clients.ToListAsync();
    }


    public async Task<Client?> GetClient(int ClientId){
        return await _context.Clients.FindAsync(ClientId);
    }


    public async Task<IEnumerable<Order>?> GetOrders(int ClientId){
        return await _context.Orders.Where(order => order.SourceId == ClientId).ToListAsync();
    }


    public async Task<Client?> AddClient(Client client){
        client.CreatedAt = DateTime.Now;
        client.UpdatedAt = DateTime.Now;
        await _context.Clients.AddAsync(client);
        await _context.SaveChangesAsync();
        return await GetClient(client.Id);
    }


    public async Task UpdateClient(int ClientId, Client client){
        client.Id = ClientId;
        client.UpdatedAt = DateTime.Now;
        _context.Clients.Update(client);
        await _context.SaveChangesAsync();
    }


    public async Task DeleteClient(int ClientId){
        Client? client = await _context.Clients.FindAsync(ClientId);
        if(client == null) return;
        _context.Clients.Remove(client);
        await _context.SaveChangesAsync();
    }



}

public interface IClientService
{
    Task<IEnumerable<Client>?> GetClients();
    Task<Client?> GetClient(int ClientId);
    Task<IEnumerable<Order>?> GetOrders(int ClientId);
    Task<Client?> AddClient(Client client);
    Task UpdateClient(int ClientId, Client client); // ASK: Why doesn't it return the created client?
    Task DeleteClient(int ClientId);
}