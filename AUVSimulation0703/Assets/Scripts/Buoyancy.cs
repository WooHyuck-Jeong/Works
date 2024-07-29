using UnityEngine;

public class Buoyancy : MonoBehaviour
{
    public float waterLevel = 0f; // 물의 높이
    public float waterDensity = 1000f; // 물의 밀도, kg/m^3
    public float buoyancyFactor = 1f; // 부력 계수

    private Rigidbody rb;
    private float objectVolume; // 물체의 부피

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        CalculateVolume();
    }

    void CalculateVolume()
    {
        // 실린더의 부피 계산
        float radius = transform.localScale.x / 2;
        float height = transform.localScale.y;
        objectVolume = Mathf.PI * Mathf.Pow(radius, 2) * height;
    }

    void FixedUpdate()
    {
        if (transform.position.y < waterLevel)
        {
            float submergedVolume = objectVolume * Mathf.Clamp01((waterLevel - transform.position.y) / transform.localScale.y);
            Vector3 buoyancy = waterDensity * submergedVolume * Physics.gravity * -1 * buoyancyFactor;
            rb.AddForce(buoyancy, ForceMode.Acceleration);
        }
    }
}